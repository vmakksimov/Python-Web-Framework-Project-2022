from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out

from Crypto_web.accounts.models import Profile


@receiver(user_logged_out, sender=Profile)
def logout_user(sender, user, request, **kwargs):
    a = sender
    b = user
    c = request
    print(f'Log Oout {user}')