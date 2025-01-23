from django.contrib import admin
from .models import Reviews


# Register your models here.
@admin.register(Reviews)
class ReviewsConfig(admin.ModelAdmin):
    pass
