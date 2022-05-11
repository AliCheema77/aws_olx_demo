from django.db import models
from django.contrib.auth import get_user_model
from products.models import Post

User = get_user_model()


class PurchasedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='purchase_post')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    price = models.FloatField()
