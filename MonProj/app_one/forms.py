from django import forms
from .models import User_Authentication


class LoginForm(forms.Form):
    phone_or_email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder':'Phone/Email',
                'class':'form-control mr-sm-2',
                'id': 'Phone_Email',
            }),
        label='',
        required=True
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'password',
                'placeholder':'Password',
                'class':'form-control mr-sm-2',
                'id': 'Password',
            }),
        label='',
        required=True
    )

class user_login(forms.ModelForm):
    class Meta:
        model = User_Authentication
        fields = ('phone', 'email', 'password')
