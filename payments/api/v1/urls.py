from django.urls import path

from payments.api.v1.viewsets import SubscriptionCard, BuyAndSellView

urlpatterns = [
    path('payment/<int:post_id>/', SubscriptionCard.as_view(), name='payment'),
    path('purchase_sell_product/<int:user_id>/', BuyAndSellView.as_view(), name='purchase_sell_product')
]
