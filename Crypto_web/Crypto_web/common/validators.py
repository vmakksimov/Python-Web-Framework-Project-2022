
import string

from django.core.exceptions import ValidationError



def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_alphabet_characters_english(value):
    for char in value.lower():
        if char.isalpha() and char not in string.ascii_lowercase:
            raise ValidationError('You are not allowed to use non-English characters')



def validate_if_number_starts_with_country_code(value):
    country_code = value[0]
    number = value[1:]
    if not country_code == '+':
        raise ValidationError('You number must start with your country code including "+" in front.')
    for char in number:
        if not char.isdigit():
            raise ValidationError('You must input only digits.')


def validate_coin(coins, request, kwargs):
    for el in coins:
        if kwargs == el.pk:
            current_value = float(request['quantity'])
            if current_value > el.quantity:
                raise ValidationError(
                    'You don\'t have than much quantity on this coin. Please submit different amount.')
            elif current_value == el.quantity:
                return 'False'

            price = 0
            if el.type == 'Solana':
                price = float(el.SOL_CURRENT_PRICE)
            elif el.type == 'Bitcoin':
                price = float(el.BITCOIN_CURRENT_PRICE)
            elif el.type == 'BNB':
                price = float(el.BNB_CURRENT_PRICE)
            elif el.type == 'Dash':
                price = float(el.DASH_CURRENT_PRICE)
            elif el.type == 'Polkadot':
                price = float(el.POLK_CURRENT_PRICE)
            elif el.type == 'Bitcoin':
                price = float(el.BITCOIN_CURRENT_PRICE)
            elif el.type == 'Ethereum':
                price = float(el.BITCOIN_CURRENT_PRICE)

            request['fiat_value'] = float(request['quantity']) * price
            new = str(round(float(el.quantity) - float(request['quantity']), 4))

            request['quantity'] = new
            break

    return request


def validate_coin_converter_all(coins, request, kwargs):
    for el in coins:
        if kwargs == el.pk:
            current_value = el.quantity
            price = 0
            if el.type == 'Solana':
                price = float(el.SOL_CURRENT_PRICE)
            elif el.type == 'Bitcoin':
                price = float(el.BITCOIN_CURRENT_PRICE)
            elif el.type == 'BNB':
                price = float(el.BNB_CURRENT_PRICE)
            elif el.type == 'Dash':
                price = float(el.DASH_CURRENT_PRICE)
            elif el.type == 'Polkadot':
                price = float(el.POLK_CURRENT_PRICE)
            elif el.type == 'Bitcoin':
                price = float(el.BITCOIN_CURRENT_PRICE)
            elif el.type == 'Ethereum':
                price = float(el.BITCOIN_CURRENT_PRICE)

            request['fiat_value'] = current_value * price
            break

    return request






