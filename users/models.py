from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):  # 선택항목 칼럼을 만들 때 필요함함
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    class LanguageChoices(models.TextChoices):
        KO = "ko", "Korean"
        EN = "en", "English"

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    pofile_photo = models.ImageField(blank=True)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)

    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    curreny = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
