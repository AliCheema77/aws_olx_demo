from celery import shared_task
import requests
import json
from products.models import Post
from datetime import date, datetime
from olx_demo.pushers import notify_me


@shared_task()
def project_results():
    try:
        posts = Post.objects.all()
        for post in posts:
            created = datetime.strptime(str(post.created.replace(microsecond=0, tzinfo=None)),
                                        "%Y-%m-%d %I:%M:%S").date()
            today = date.today()
            difference = today-created
            if difference.days >= 15 and post.status != "inactive":
                post.status = "inactive"
                post.save()
                notify_me(post.user.username, "Your post is Inactive")
                print(post.status)

    except Exception as e:
        print(e)
