from django import forms
from Crypto_web.common.helpers import BootstrapFormMixin
from Crypto_web.helparticle.models import HelpArticle


class CreateArticleForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        article = super().save(commit=False)
        article.user = self.user
        if commit:
            article.save()

        return article

    class Meta:
        model = HelpArticle
        fields = ('title', 'image', 'description')


class UpdateArticleForm(BootstrapFormMixin, forms.ModelForm):
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
        model = HelpArticle
        fields = ('title', 'image', 'description')


class DeleteArticleForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = HelpArticle
        fields = ()