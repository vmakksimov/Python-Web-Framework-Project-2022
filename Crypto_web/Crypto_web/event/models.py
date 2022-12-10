from django.db import models

from Crypto_web.common.validators import validate_alphabet_characters_english


# Create your models here.
class CryptoEvent(models.Model):
    title = models.CharField(
        max_length=100,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    description = models.CharField(
        max_length=200,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    is_event_of_month = models.BooleanField(
        default=False,
    )


    event_image = models.URLField(

    )

    event_date = models.DateField()

    class Meta:
        verbose_name = 'Event'

    def __str__(self):
        return self.title