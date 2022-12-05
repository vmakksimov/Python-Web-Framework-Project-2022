from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from Crypto_web.common.helpers import BootstrapFormMixin
from Crypto_web.accounts.models import Profile, CryptoUser


class ProfileForms(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,

    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField()
    date_of_birth = forms.DateField()

    description = forms.CharField(
        widget=forms.Textarea,
    )

    email = forms.EmailField()

    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],

            description=self.cleaned_data['description'],

            email=self.cleaned_data['email'],

            gender=self.cleaned_data['gender'],
            user=user
        )

        if commit:
            profile.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter First Name'
                }

            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Last Name'
                }
            ),

            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }
            )

        }


class DeleteForm(forms.ModelForm):

    def save(self, commit=True):
        profile = self.instance
        users = CryptoUser.objects.all()
        current_user = users.filter(username=profile.user)

        current_user.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user = self.user
        if commit:
            profile.save()

        return profile

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'description','picture', 'email', 'gender',)
