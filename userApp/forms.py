from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address',
            'date_of_birth',
            'phone',
            'gender',
            'profile_picture',
            'state_of_origin',
            'country'
        ]

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address',
            'date_of_birth',
            'phone',
            'gender',
            'profile_picture',
            'state_of_origin',
            'country',
            'valid_id_card',
            'proof_of_registration',
            'role'
        ]