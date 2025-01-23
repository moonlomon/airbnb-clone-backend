from django.contrib import admin
from rooms.models import Room, Amenity


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_filter = (
        "name",
        "country",
        "rooms",
        "toilets",
        "address",
        "kind",
        "owner",
        "amenities",
    )

    list_display = (
        "name",
        "price",
        "owner",
        "create_at",
        "update_at",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "create_at",
        "update_at",
    )
    readonly_fields = (
        "create_at",
        "update_at",
    )
