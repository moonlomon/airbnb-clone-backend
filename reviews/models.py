from django.db import models
from common.models import CommonModel
from config.settings import AUTH_USER_MODEL, AUTH_FOREIEGN_KEYS
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Reviews(CommonModel):
    """Reviews from User to Room and Experience"""

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    room = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Room"],
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    experience = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Experience"],
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    payload = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return f"{self.user} {self.room} (평점:{self.rating})"

    class Meta:
        verbose_name_plural = "Reviews"
