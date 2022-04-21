from django.shortcuts import render,redirect
from math import ceil
from django.contrib.auth.models import User
from .forms import RegisterForm,ProfileForm,OrdersForm,ProductForm,OrderUpdateForm
from .models import Profile,Orders,Product,OrderUpdate  
# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():

            form.save()
           
            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})


def products(request):
    products = Product.objects.values('category', 'id')
    current_user = request.user
    return render(request,'product.html',{ "products":products})
    

