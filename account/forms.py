from django import forms
from .models import Account


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])

        user.save()

        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name')