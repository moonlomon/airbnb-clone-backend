from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):  # 유저 클래스만 admin을 UserAdmin을 상속.
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "pofile_photo",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "curreny",
                ),
            },
        ),
        (
            "Permission",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "name", "email", "is_host")


# Register your models here.
