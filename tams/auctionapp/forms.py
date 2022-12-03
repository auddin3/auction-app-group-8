from django.forms import ModelForm
from auctionapp.models import User
from django import forms

class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'padding: 5px; margin: 10px; border-radius: 25px;'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'style': 'padding: 5px; margin: 10px; border-radius: 25px;',
            }),
            'email': forms.TextInput(attrs={
                'style': 'padding: 5px; margin: 10px; border-radius: 25px;',
            }),
            'first_name': forms.TextInput(attrs={
                'style': 'padding: 5px; margin: 10px; border-radius: 25px',
            }),
            'last_name': forms.TextInput(attrs={
                'style': 'padding: 5px; margin: 10px; border-radius: 25px',
            }),
            'password': forms.PasswordInput(attrs={
                'style': 'padding: 5px; margin: 10px; border-radius: 25px',
            })
        }

class LogInForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'padding: 5px; margin: 10px; border-radius: 25px;'}))
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
            'style': 'padding: 5px; margin: 10px; border-radius: 25px;',}),    
        }