from django.db import models

from Crypto_web.common.validators import validate_alphabet_characters_english


# Create your models here.

class HelpArticle(models.Model):
    TITLE_MAX_CH = 30
    DESCRIPTION_MAX = 1000

    title = models.CharField(
        max_length=TITLE_MAX_CH,
    )

    name = models.CharField(
        max_length=10,
    )

    image = models.URLField()

    description = models.TextField(
        max_length=DESCRIPTION_MAX,
        validators=(
            validate_alphabet_characters_english,
        ),
        blank=True,
        null=True,
    )

    date_created = models.DateField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Help Article'
