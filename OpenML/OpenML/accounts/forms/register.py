from django import forms
from OpenML.accounts.models import User
from django.db import models as db_models


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    email = forms.EmailField(widget=forms.widgets.TextInput, label='Email')
    firstname = forms.CharField(widget=forms.widgets.TextInput, label='First Name')
    lastname = forms.CharField(widget=forms.widgets.TextInput, label='Last Name')
    password1 = forms.CharField(widget=forms.widgets.PasswordInput,label="password1")
    password2 = forms.CharField(widget=forms.widgets.PasswordInput,label="password2")


    class Meta:
        model = User
        fields = ['email','firstname', 'lastname',]

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

