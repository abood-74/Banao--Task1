
from django import forms
from django.core.exceptions import ValidationError
from .models import User
#import make password hash
from django.contrib.auth.hashers import make_password

class SignUpForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password', 'password_confirm', 'city', 'state', 'pincode', 'user_type']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise ValidationError("Passwords do not match.")
        cleaned_data[password] = make_password(password)
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data.get('password'))
        if commit:
            instance.save()
        return instance

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
