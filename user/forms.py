import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from user.models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_image', 'bio']
        widgets = {
            'user': forms.TextInput(attrs={'value':'', 'id':'blogger', 'type':'hidden'}),
            'bio':forms.Textarea(attrs={'rows':15, 'col':50}),
        }