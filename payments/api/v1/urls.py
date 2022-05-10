from django.urls import path

from payments.api.v1.viewsets import SubscriptionCard

urlpatterns = [
    path('payment/<int:post_id>/', SubscriptionCard.as_view(), name='subscription'),
]
