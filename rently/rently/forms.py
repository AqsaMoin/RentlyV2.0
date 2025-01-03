from django import forms
from product.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from product.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2']

    # Optional: Custom validation can be added here
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
       
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username, Email or Phone'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'product_category', 'product_description', 'product_price']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control'}),
            'product_category': forms.Select(attrs={'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }
