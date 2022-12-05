from django.contrib import admin

from Crypto_web.news.models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('author',)
    list_filter = ('author',)