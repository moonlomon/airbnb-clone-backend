from django.db import models
from common.models import CommonModel


# Create your models here.
class Categories(CommonModel):
    """Room or Exprience Categories"""

    class CategoriesKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIECES = "experiences", "Experiences"

    name = models.CharField(max_length=250)
    kind = models.CharField(
        max_length=20,
        choices=CategoriesKindChoices.choices,
    )

    def __str__(self):
        return f"{self.kind.title()}:{self.name}"
