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
def about_us(request):
    return render(request, 'about.html')

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
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    orders = Orders.objects.filter(user=current_user).all()
    order_update = OrderUpdate.objects.filter(user=current_user).all()
    products = Product.objects.all()
    context = {'profile':profile,'orders':orders,'order_update':order_update,'products':products}
    return render(request,'profile.html',context)

   


