from django.contrib import admin
from .models import Reviews


# Register your models here.
@admin.register(Reviews)
class ReviewsConfig(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = ("rating",)
