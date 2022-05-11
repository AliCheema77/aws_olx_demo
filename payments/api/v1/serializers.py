from rest_framework import serializers
from payments.models import PurchasedProduct


class CardDetailSerializer(serializers.Serializer):
    card_number = serializers.CharField(required=True)
    card_exp_month = serializers.IntegerField(required=True)
    card_exp_year = serializers.IntegerField(required=True)
    card_cvv = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
    post_id = serializers.IntegerField(required=True)
    seller_id = serializers.IntegerField(required=True)


class PurchasedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedProduct
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        data['post'] = instance.post.ad_title
        data['seller'] = instance.user.username
        return data
