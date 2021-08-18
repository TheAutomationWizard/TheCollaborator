from django import forms
from django.contrib.auth.models import User
from .models import User_Authentication, UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('social_site', 'profile_pic')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Username',
                'class': 'form-control mr-sm-2',
                'id': 'username',
                'name': 'username'
            }),
        label='',
        required=True
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'Password',
                'placeholder': 'Password',
                'class': 'form-control mr-sm-2',
                'id': 'password',
                'name': 'password'
            }),
        label='',
        required=True
    )


class user_login(forms.ModelForm):
    class Meta:
        model = User_Authentication
        fields = ('phone', 'email', 'password')
