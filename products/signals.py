from django.db.models.signals import post_save
from olx_demo.pushers import notify_me
from products.models import Post
from django.dispatch import receiver


# @receiver(post_save, sender=Post)
# def notify_user(sender, instance, **kwargs):
#     if instance.viewed == 0 or instance.status == "inactive":
#         notify_me(instance.user.username, "Your Ad is live")
#     else:
#         pass
