from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Orders,OrderUpdate,Product
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
@login_required(login_url='login') 
def menu(request):
    return render(request,'menu.html')

def services(request):
    return render(request,'services.html')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():

            form.save()
           
            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})
def profile(request):
    return render(request,'profile.html')

def order(request):


    return render(request,'order.html')