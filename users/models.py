from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        OTHER = ("other", "Other")
    class LanguageChoices(models.TextChoices):
        EN = ("en", "English")
        KR = ("kr", "Korean")
    class CurrencyChoices(models.TextChoices):
        USD = ("usd", "Dollar")
        WON = ("won", "Korean Won")

    first_name = models.CharField(
        max_length=150, 
        editable=False, 
        blank=True,
    )
    last_name = models.CharField(
        max_length=150, 
        editable=False, 
        blank=True,
    )
    profile_photo = models.ImageField(blank=True)
    name = models.CharField(
        max_length=150, 
        blank=True,
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10, 
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
