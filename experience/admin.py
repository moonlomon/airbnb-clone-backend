from django.contrib import admin
from .models import Experience, Perk

# Register your models here.


@admin.register(Experience)
class ExprerienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "host",
        "start_at",
        "end_at",
        "price",
    )
    list_filter = ("category",)


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = ("name", "detail", "description")
