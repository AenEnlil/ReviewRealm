from django import forms
from django.contrib.auth.hashers import make_password

from .models import User


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        password = make_password(cleaned_data.get('password'))

        instance = super().save(commit=False)
        instance.password = password
        instance.save()
        return instance


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
