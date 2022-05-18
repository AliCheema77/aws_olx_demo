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
            # created = datetime.strptime(str(post.created.replace(microsecond=0, tzinfo=None)),
            #                             "%Y-%m-%d %I:%M:%S").date()
            # today = date.today()
            # difference = today-created
            # if difference.days >= 15 and post.status != "inactive":
            #     post.status = "inactive"
            #     post.save()
            #     notify_me(post.user.username, "Your post is Inactive")
            #     print(post.status)
            #     print("after success full operation celery run")
            now = datetime.strptime(str(datetime.now().replace(tzinfo=None)), "%Y-%m-%d %I:%M:%S.%f")
            created = datetime.strptime(str(post.created.replace(tzinfo=None)), "%Y-%m-%d %I:%M:%S.%f")
            difference = (now - created).seconds
            if difference >= 300 and post.status != "inactive":
                post.status = "inactive"
                post.save()
                notify_me(post.user.username, "Your post is Inactive")
                print(post.status)
                print("after success full operation celery run")
            print("celery task run")

    except Exception as e:
        print(e)
