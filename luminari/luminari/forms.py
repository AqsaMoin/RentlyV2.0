from django import forms
from django.contrib.auth.hashers import make_password
from place.models import Place
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
        

class PlaceForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('None','-----'),
        ('temple','Temple'),
        ('historic_site','Historic Site'),
        ('heritage_site','Heritage Site'),
    ]
    place_category = forms.ChoiceField(choices=CATEGORY_CHOICES,required = True,label="Place Category")
    class Meta:
        model = Place
        fields = ['place_img','place_title','place_desc','place_category']

        widgets = {
            'place_desc':forms.Textarea(attrs={'rows':4,'cols':40}),
        }


class PasswordResetForm(forms.Form):
    pass

class SetNewPasswordForm(forms.Form):
    pass