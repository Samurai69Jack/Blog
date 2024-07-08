from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    name=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name for the blog'}))
    description=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter description'}))
    image=forms.ImageField(label="",widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}))

    class Meta:
        model=Blog
        fields=['name','description','image']



class SignupForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter username'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}))

    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2','username']
    
