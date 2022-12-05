from django.contrib import admin

from Crypto_web.web.models import Coin, Deposit, ContactUs


# Register your models here.
@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('type', 'quantity')

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('currency', 'amount')
    ordering = ('amount',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)