from django import forms
from Crypto_web.common.helpers import BootstrapFormMixin
from Crypto_web.event.models import CryptoEvent
from Crypto_web.helparticle.models import HelpArticle

class CreateEventForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        event = super().save(commit=False)
        event.user = self.user
        if commit:
            event.save()

        return event

    class Meta:
        model = CryptoEvent
        fields = ('title', 'description', 'event_image', 'event_date',)


class UpdateEventForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        event = super().save(commit=False)
        event.user = self.user
        if commit:
            event.save()

        return event

    class Meta:
        model = CryptoEvent
        fields = ('title', 'description', 'event_image', 'event_date',)



class DeleteEventForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = CryptoEvent
        fields = ()