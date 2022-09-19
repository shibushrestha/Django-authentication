from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages={
        'password_mismatch':"Please enter same passwords.",
        }
        self.fields['password1'].widget.attrs.update({
            'placeholder':"Enter a password",
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':"Confirm password", 
        })
        self.fields['email'].required = True

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter a username',}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Your first name',}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your last name',}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a email address',}),
        }
        error_messages={
            'username':{
                'unique':"Username already taken.",
                'required':"Enter a username.",
            },
            'first_name':{
                'required':"Enter your first name."
            },
            'email':{
                'required':'Enter a email address',
                'invalid':'Please enter a valid email address'
            }
        }
        
