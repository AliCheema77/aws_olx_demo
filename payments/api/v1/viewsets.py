from datetime import timedelta
import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone
from djstripe.models import Plan, Subscription, Customer, PaymentMethod
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from payments.api.v1.serializers import CardDetailSerializer, PurchasedProductSerializer
from payments.models import PurchasedProduct
from products.models import Post

stripe.api_key = settings.STRIPE_API_KEY
User = get_user_model()


class SubscriptionCard(ListCreateAPIView):
    serializer_class = CardDetailSerializer
    queryset = User.objects.none

    def get(self, request, *args, **kwargs):
        return Response()

    def post(self, request, *args, post_id=None, **kwargs):
        if request.user.is_authenticated:
            post = Post.objects.get(id=post_id)
            user = request.user
            serializer = CardDetailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            try:
                token = stripe.Token.create(
                    card={
                        "number": data.get("card_number"),
                        "exp_month": data.get("card_exp_month"),
                        "exp_year": data.get("card_exp_year"),
                        "cvc": data.get("card_cvv")
                    }, )
                try:
                    price = int(post.price/187)
                    stripe.Charge.create(
                        amount=price,
                        currency="usd",
                        source="tok_visa",
                        description="My First Test Charge (created for API docs)",
                    )
                    purchase_product = PurchasedProduct(user=user, post=post, seller=post.user, price=post.price)
                    purchase_product.save()
                    return Response({"response": f"Transaction of pkr {post.price} has been succeeded "}, status=status.HTTP_200_OK)
                except stripe.error.CardError as e:
                    return Response({"response": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
            except stripe.error.CardError as e:
                return Response({"response": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": "Please login first"}, status=status.HTTP_400_BAD_REQUEST)


class BuyAndSellView(APIView):
    serializer_class = PurchasedProductSerializer

    def get(self, request, user_id=None):
        user_posts = {}
        if user_id is not None:
            posts = PurchasedProduct.objects.all()
            buy_by_user = self.serializer_class(posts.filter(user_id__exact=user_id), many=True)
            user_posts["buy_by_user"] = buy_by_user.data
            sell_by_user = self.serializer_class(posts.filter(seller_id__exact=user_id), many=True)
            user_posts["sell_by_user"] = sell_by_user.data
            return Response({"response": user_posts}, status=status.HTTP_200_OK)
        return Response({"response": f"{user_id} is not exist"})



