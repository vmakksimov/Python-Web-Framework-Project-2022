from django.contrib import admin

from Crypto_web.helparticle.models import HelpArticle


# Register your models here.

@admin.register(HelpArticle)
class HelpArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)

    ordering = ('title',)
    search_fields = ('title',)
    list_per_page = 5
