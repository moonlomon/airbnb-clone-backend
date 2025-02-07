from django.contrib import admin
from .models import Bookings


# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "kind",
        "room",
        "experience",
        "check_in",
        "check_out",
        "experiece_date",
        "guest",
    )

    list_filter = ("kind",)
