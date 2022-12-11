from django.db import models

# Create your models here.
class Partners(models.Model):
    NAME_MAX_CH = 30

    name = models.CharField(
        max_length=NAME_MAX_CH,
        blank=False,
        null=False,
    )

    image = models.URLField()

    date_created = models.DateField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Partners'