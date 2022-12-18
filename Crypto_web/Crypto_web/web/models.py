import random

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


from Crypto_web.common.validators import validate_alphabet_characters_english, \
    validate_if_number_starts_with_country_code


# Create your models here.

UserModel = get_user_model()


class Coin(models.Model):
    BTC_CURRENT_PRICE = random.randint(16151, 16895)
    ETH_CURRENT_PRICE = random.randint(1105, 1854)
    BNB_CURRENT_PRICE = random.randint(250, 376)
    SOL_CURRENT_PRICE = random.randint(14, 97)
    POLK_CURRENT_PRICE = random.randint(5, 15)
    DASH_CURRENT_PRICE = random.randint(40, 98)
    AVA_CURRENT_PRICE = random.randint(40, 98)

    STATUS = (
        (BTC_CURRENT_PRICE, _('Bitcoin')),
        (ETH_CURRENT_PRICE, _('Ethereum')),
        (BNB_CURRENT_PRICE, _('Solana')),
        (SOL_CURRENT_PRICE, _('BNB')),
        (POLK_CURRENT_PRICE, _('Polkadot')),
        (DASH_CURRENT_PRICE, _('Dash')),
        (AVA_CURRENT_PRICE, _('Avalanche')),
    )

    WALLET_ADDRESS_MAX_LENGTH = 64
    CARD_MAX_LENGTH = 20
    MAX_LENGTH = 10000000
    MIN_VALUE = 0.00000001
    MAX_VALUE = 10000
    COIN_NAME_MAX_LENGTH = 30
    IBAN = 34

    BITCOIN = 'Bitcoin'
    ETH = 'Ethereum'
    SOL = 'Solana'
    BNB = 'BNB'
    POLKADOT = 'Polkadot'
    DASH = 'Dash'
    AVA = 'Avalanche'
    TYPES = [(x, x) for x in (BITCOIN, ETH, SOL, BNB, POLKADOT, DASH, AVA)]

    BITCOIN_CURRENT_PRICE = BTC_CURRENT_PRICE
    ETH_PRICE = ETH_CURRENT_PRICE
    BNB = BNB_CURRENT_PRICE
    SOL = SOL_CURRENT_PRICE
    POLKADOT = POLK_CURRENT_PRICE
    DASH = DASH_CURRENT_PRICE
    COINS_PRICES = [(x, x) for x in (BITCOIN_CURRENT_PRICE, ETH_PRICE, BNB, SOL, POLKADOT, DASH)]

    ERC20 = 'ERC20'
    BSC = 'Binance Smart Chain'
    POLYGON = 'Polygon'
    BEP2 = 'BEP2'

    NETWORK = [(x, x) for x in (ERC20, BSC, POLYGON, BEP2)]

    VISA = 'Visa'
    MASTERCARD = 'MasterCard'


    METHODS = [(x, x) for x in (VISA, MASTERCARD)]

    quantity = models.FloatField(
        max_length=MAX_LENGTH,
        validators=(
            MinValueValidator(MIN_VALUE),
            MaxValueValidator(MAX_VALUE),

        )

    )

    fiat_value = models.CharField(
        max_length=1000000,
        null=True,
        blank=True,
        verbose_name= 'Previous Fiat Value'
    )

    network = models.CharField(
        max_length=max(len(x) for (x, _) in NETWORK),

        choices=NETWORK
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )

    wallet_address = models.CharField(
        max_length=WALLET_ADDRESS_MAX_LENGTH,
        blank=True,
        null=True,

    )

    payment_method = models.CharField(
        max_length=max(len(x) for (x, _) in METHODS),

        choices=METHODS
    )

    # TO CHeck for the correct way
    card_number = models.CharField(
        max_length=CARD_MAX_LENGTH,
        validators=(
            MinLengthValidator(5),
        ),
        null=False,
        blank=False,
    )

    iban = models.CharField(
        max_length=IBAN,
        validators=(
            MinLengthValidator(5),
        ),
        null=False,
        blank=False,
        verbose_name='IBAN',
    )

    cvv = models.CharField(
        max_length=3,
        validators=(
            MinLengthValidator(3),
        ),
        null=False,
        blank=False,
        verbose_name='CVV',
    )

    coin_prices = models.IntegerField(
        null=True,
        blank=True,
        choices=(
            ('Solana', SOL_CURRENT_PRICE),
            ('Bitcoin', BITCOIN_CURRENT_PRICE),
            ('Ethereum', ETH_CURRENT_PRICE),
            ('BNB', BNB_CURRENT_PRICE),
            ('Polkadot', POLK_CURRENT_PRICE),
            ('Dash', DASH_CURRENT_PRICE),
            ('Avalanche', AVA_CURRENT_PRICE),
        )
    )

    coin_prices_two = models.PositiveSmallIntegerField(
        default=1,
        choices=STATUS,
    )


    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.type


    class Meta:
        verbose_name = 'Coin'


class Deposit(models.Model):
    MAX_LENGTH_DEPOSIT = 9

    NAME_LENGTH = 50
    IBAN_LENGTH = 34
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
    BIC_SWIFT_LENGTH = 11

    TYPES = [(x, x) for x in (EUR, USD, GBP)]

    amount = models.FloatField(
        default=0,
        max_length=7,
        null=True,
        blank=True,


    )

    currency = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),

        choices=TYPES
    )

    beneficiary_name = models.CharField(
        max_length=NAME_LENGTH,
        null=False,
        blank=False,
    )

    iban = models.CharField(
        max_length=IBAN_LENGTH,
        null=False,
        blank=False,
    )


    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )



    class Meta:
        verbose_name = 'Fiat Wallet'


class ContactUs(models.Model):
    TITLE_MAX_CH = 20
    MAX_LENGTH = 13
    MIN_LENGTH = 10

    name = models.CharField(
        max_length=TITLE_MAX_CH,
        null=False,
        blank=False,
    )

    mobile_number = models.CharField(
        max_length=MAX_LENGTH,
        validators=(
            validate_if_number_starts_with_country_code,
            MinLengthValidator(MIN_LENGTH, message='The number is incorrect.')
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    message = models.TextField(
        blank=False,
        null=False,
    )
    time = models.TimeField(
        auto_now_add=True,

    )

    author = models.ForeignKey(
      UserModel,
      on_delete=models.CASCADE,
      default=1,
      db_constraint=False,
     )

    class Meta:
        verbose_name = 'Contact Us'


