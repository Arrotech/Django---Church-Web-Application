from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """[summary]

    Args:
        UserCreationForm ([type]): [description]
    """
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.CharField()

    class Meta:
        """[summary]
        """
        model = User
        fields = ['username', 'email', 'firstname',
                 'lastname', 'phone', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    phone = forms.CharField()

    class Meta:
        """[summary]
        """
        model = User
        fields = ['username', 'email', 'firstname',
                 'lastname', 'phone']  

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']