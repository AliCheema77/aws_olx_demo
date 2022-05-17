from django.db.models.signals import post_save
from olx_demo.pushers import ad_post_notification
from products.models import Post
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def notify_user(sender, instance, **kwargs):
    print("send notification")
    ad_post_notification(instance, instance.user.username)


