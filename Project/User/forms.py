from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':"Enter a username"})
        self.fields['first_name'].widget.attrs.update({'placeholder':"Your first name"})
        self.fields['first_name'].required = True
        self.fields['last_name'].widget.attrs.update({'placeholder':"Your last name"})
        self.fields['last_name'].required = True
        self.fields['email'].widget.attrs.update({'placeholder':"Enter a email address"})
        self.fields['email'].required = True
        self.fields['password'].widget.attrs.update({'placeholder':"Enter password"})
        self.fields['password2'].widget.attrs.update({'placeholder':"Confirm password"})

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password",)
        widgets = {
            'password' : forms.PasswordInput
        }
        error_messages={
            'username':{
                'unique':"Username already taken.",
            },
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError(_("Please enter same passwords."), code="password_mismatch")
