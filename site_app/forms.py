from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label='Password', widget=forms)
    role_choise = forms.Select(choices=(('Seller', 'Seller'), ('Buyer', 'Buyer')))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role_choise')
