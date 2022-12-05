from Crypto_web.accounts.models import Profile
from Crypto_web.web.models import Coin


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def get_coins():
    coins = Coin.objects.all()
    if coins:
        return coins
    else:
        return None


def get_unique_object(value):
    unique_object = {}

    if value is None:
        return None

    for el in value:
        if el.type not in value:
            unique_object[el.type] = el.quantity
        else:
            unique_object[el.type] += el.quantity

    return unique_object


def calculate_total_balance(coins):
    total_balance = 0
    for el in coins:
        for stat in el.STATUS:
            if str(el) == str(stat[1]):
                total_balance += stat[0]
                break

    return total_balance
