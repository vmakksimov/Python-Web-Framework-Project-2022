from django import forms
from Crypto_web.common.helpers import BootstrapFormMixin

from Crypto_web.partners.models import Partners


class CreatePartnersForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        partners = super().save(commit=False)
        partners.user = self.user
        if commit:
            partners.save()

        return partners

    class Meta:
        model = Partners
        fields = ('name', 'image',)

class DeletePartnersForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Partners
        fields = ()