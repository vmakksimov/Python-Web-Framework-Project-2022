
from django import forms
from Crypto_web.common.helpers import BootstrapFormMixin
from Crypto_web.web.models import Coin, ContactUs, Deposit


class CreateCoinForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        coin = super().save(commit=False)
        coin.user = self.user
        if commit:
            coin.save()

        return coin

    class Meta:
        model = Coin
        fields = ('quantity', 'type', 'payment_method', 'card_number', 'iban', 'cvv',)

        widgets = {
            'wallet_address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter wallet address to withdraw. (0x821...)',
                    'rows': 1
                })
        }


class CreateContactForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        contact = super().save(commit=False)
        contact.user = self.user
        if commit:
            contact.save()

        return contact

    class Meta:
        model = ContactUs
        fields = ('name', 'mobile_number', 'email', 'message')
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Input your message here',
                    'rows': 5
                }),
            'name': forms.Textarea(
                attrs={
                    'placeholder': 'Input your name here',
                    'rows': 1

                }),
            'mobile_number': forms.Textarea(
                attrs={
                    'placeholder': 'Input your phone number here',
                    'rows': 1

                }),
            'email': forms.Textarea(
                attrs={
                    'placeholder': 'Input your email here',
                    'rows': 1

                })
        }


class UpdateCoinForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        coin = super().save(commit=False)
        coin.user = self.user
        if commit:
            coin.save()

        return coin

    class Meta:
        model = Coin
        fields = ('quantity',)


class WithdrawCoinForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Coin
        fields = ('wallet_address',)
        widgets = {
            'wallet_address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter wallet address to withdraw. (0x821...)',
                    'rows': 1
                })
        }

class WithdrawAllCoinConvertedForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Coin
        fields = ('fiat_value',)
        widgets = {
            'fiat_value': forms.Textarea(
                attrs={
                    'placeholder': 'Click on "Withdraw" to continue.',
                    'rows': 1
                })
        }


class CreateDepositForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()
        for name, field in self.fields.items():
            field.required = False

    def save(self, commit=True):
        deposit = super().save(commit=False)
        deposit.user = self.user
        if commit:
            deposit.save()

        return deposit

    class Meta:
        model = Deposit
        fields = ('currency', 'beneficiary_name',)

        widgets = {
            'beneficiary_name': forms.Textarea(
                attrs={
                    'placeholder': 'The legal name you used to register in our app (this must be your full name, as registered in your personal bank account)',
                    'rows': 1
                }),
            'iban': forms.Textarea(
                attrs={
                    'placeholder': 'this is your IBAN.',
                    'rows': 1

                }),
            'bic_swift_code': forms.Textarea(
                attrs={
                    'placeholder': 'Some banks require it to transfer the money',
                    'rows': 1

                }),
        }


class ConvertCoinForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for name, field in self.fields.items():
            if name == 'type':
                field.disabled = True

    class Meta:
        model = Coin
        fields = ('quantity', 'type', 'fiat_value')
        widgets = {
            'wallet_address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter wallet address to withdraw. (0x821...)',
                    'rows': 1
                })
        }


class ConvertFiatForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        for name, field in self.fields.items():
            field.required = False
            field.readonly = True

    class Meta:
        model = Deposit
        fields = ('amount',)
        deposit_amount = forms.ModelChoiceField(queryset=Deposit.objects.all(),
                                                label='Current Amount (click Submit to add the crpypto amount).')



class WithdrawFiatForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Deposit
        fields = ('amount','beneficiary_name', 'iban', 'currency')
        widgets = {
            'beneficiary_name': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the first and last name assosiated with your bank account.',
                    'rows': 1,

                }),
            'iban': forms.Textarea(
                attrs={
                    'placeholder': 'Enter the IBAN of your account.',
                    'rows': 1,

                })
        }


class DeleteMessageForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = ContactUs
        fields = ()

