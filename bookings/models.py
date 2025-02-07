from django.db import models
from common.models import CommonModel
from config.settings import AUTH_USER_MODEL, AUTH_FOREIEGN_KEYS


# Create your models here.
class Bookings(CommonModel):
    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = (
            "room",
            "Room",
        )
        EXPERIENCE = (
            "experience",
            "Expereince",
        )

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    kind = models.CharField(
        max_length=20, choices=BookingKindChoices.choices, default=1
    )

    room = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Room"],
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Experience"],
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    check_in = models.DateField(
        null=True,
        blank=True,
    )

    check_out = models.DateField(
        null=True,
        blank=True,
    )

    experiece_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    guest = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.kind.title()} / {self.user}"

    class Meta:
        verbose_name_plural = "Bookings"
