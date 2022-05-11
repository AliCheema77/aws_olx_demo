from django.contrib import admin
from payments.models import PurchasedProduct

# Register your models here.

@admin.register(PurchasedProduct)
class PurchaseProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'seller']
