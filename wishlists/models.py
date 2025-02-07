from django.db import models
from common.models import CommonModel
from config.settings import AUTH_USER_MODEL, AUTH_FOREIEGN_KEYS


# Create your models here.
class WishLists(CommonModel):

    name = models.CharField(max_length=150)

    rooms = models.ManyToManyField(
        AUTH_FOREIEGN_KEYS["Room"],
    )

    experience = models.ManyToManyField(
        AUTH_FOREIEGN_KEYS["Experience"],
    )

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Wish lists"
