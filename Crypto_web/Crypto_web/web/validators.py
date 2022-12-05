import string

from django.core.exceptions import ValidationError


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




