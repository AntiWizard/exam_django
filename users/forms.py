from django import forms

from users.models import User


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "username"}), label="username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password"}), label="password")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password confirm"}),
                                label="password confirm")

    class Meta:
        model = User
        fields = ('username', 'password', 'password1')


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "username"}), label="username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password"}))

    class Meta:
        model = User
        fields = ('username', 'password')
