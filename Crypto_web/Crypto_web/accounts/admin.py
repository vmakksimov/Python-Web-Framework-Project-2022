from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User

from Crypto_web.accounts.models import Profile, CryptoUser
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.

def apply_change(modeladmin, request, queryset):
    for user in queryset:
        if user.user.is_staff == False:
            user.user.is_staff = True
            user.user.save()
            user.save()


apply_change.short_description = 'Make Staff Member'


@admin.register(CryptoUser)
class CryptoUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_superuser', 'is_staff')
    list_filter = ('is_staff', 'username',)
    list_per_page = 2

    search_fields = ('username',)
    ordering = ('is_superuser',)




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',)
    list_filter = ('first_name',)
    ordering = ('first_name',)
    search_fields = ('first_name',)
    list_per_page = 5
    actions = [apply_change,]


User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance




admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
