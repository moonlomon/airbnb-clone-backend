from django.db import models
from common.models import CommonModel
from config import settings
from config.settings import AUTH_FOREIEGN_KEYS

# Create your models here.


class Experience(CommonModel):
    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=50,
        default="서울",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.TextField()

    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start_at = models.TimeField()
    end_at = models.TimeField()

    perk = models.ManyToManyField(
        "experience.Perk",
    )

    category = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Category"],
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """What is included on an experience"""

    name = models.CharField(max_length=250)
    detail = models.CharField(max_length=250, default="", blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
