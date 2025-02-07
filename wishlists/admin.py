from django.contrib import admin
from .models import WishLists


# Register your models here.
@admin.register(WishLists)
class WishListsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "create_at",
        "update_at",
    )
