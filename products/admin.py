from django.contrib import admin
from products.models import Category, SubCategory, PostImage, Post, Notification


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['ad_title', 'description', 'latitude', 'longitude', 'created', 'updated']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['view_date', "viewer_user_id", "viewer_username", "viewer_user_avatar", "post_created_date",
                    "post_username", "post_user_avatar", "post_user_id", "post_id", "text", "type", "created"]

