from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Orders,Product,OrderUpdate

class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=["username","email","password1","password2"]




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','image','desc','phone','email'] 



class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields=['name','amount','address','city','phone','email','zip_code'] 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['product_name','category','price','desc','image'] 

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = OrderUpdate
     

        fields=['order_id']         

