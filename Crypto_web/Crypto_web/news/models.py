from django.db import models


# Create your models here.
class News(models.Model):
    TITLE_MAX_LENGTH = 70
    AUTHOR_MAX_LENGTH = 20

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=True,
        blank=True,

    )

    description = models.TextField(
        blank=False,
        null=False
    )

    author = models.CharField(
        max_length=AUTHOR_MAX_LENGTH,
        blank=False,
        null=False,
    )

    current_date = models.DateTimeField(
        auto_now_add=True,
    )


    class Meta:
        verbose_name = 'News'