from django.db import models
from config.settings import AUTH_USER_MODEL, AUTH_FOREIEGN_KEYS
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    """Room Model Difinition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = (
            "entire_place",
            "Entire Place",
        )
        PRIVATE_ROOM = (
            "private_room",
            "Private Room",
        )
        SHARED_ROOM = (
            "shared_room",
            "Shared Room",
        )

    name = models.CharField(max_length=150, default="")
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=50,
        default="서울",
    )
    price = models.PositiveBigIntegerField()
    rooms = models.PositiveBigIntegerField()
    toilets = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pets_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )
    category = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Category"],
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Amenity(CommonModel):
    """Amenity Description"""

    name = models.CharField(
        max_length=150,
    )
    description = models.TextField(
        max_length=150,
        default="",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
