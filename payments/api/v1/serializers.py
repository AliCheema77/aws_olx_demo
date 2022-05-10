from rest_framework import serializers


class CardDetailSerializer(serializers.Serializer):
    card_number = serializers.CharField(required=True)
    card_exp_month = serializers.IntegerField(required=True)
    card_exp_year = serializers.IntegerField(required=True)
    card_cvv = serializers.IntegerField(required=True)