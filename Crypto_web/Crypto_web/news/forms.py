from django import forms

from Crypto_web.common.helpers import BootstrapFormMixin
from Crypto_web.news.models import News


class CreateNewsForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        news = super().save(commit=False)
        news.user = self.user
        if commit:
            news.save()

        return news

    class Meta:
        model = News
        fields = ('title', 'description', 'author',)



class UpdateNewsForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        news = super().save(commit=False)
        news.user = self.user
        if commit:
            news.save()

        return news

    class Meta:
        model = News
        fields = ('title', 'description', 'author',)


class DeleteNewsForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = News
        fields = ()