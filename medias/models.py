from django.db import models
from common.models import CommonModel
from config.settings import AUTH_FOREIEGN_KEYS


# Create your models here.
class Photo(CommonModel):

    file = models.ImageField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Room"],
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        AUTH_FOREIEGN_KEYS["Experience"],
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
