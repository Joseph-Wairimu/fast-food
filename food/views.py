from django.shortcuts import render,redirect

from math import ceil
from django.contrib.auth.models import User
from .forms import RegisterForm,ProfileForm,OrdersForm,ProductForm,OrderUpdateForm
 

from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Orders,OrderUpdate,Product

# Create your views here.
def index(request):
    return render(request, 'index.html')
    

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



def products(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    fastfood = {'allProds': allProds}
    return render(request,'product.html',fastfood)
    

# def productView(request, myid):
#     try:
#         product = Product.objects.filter(id=myid)
#     except ObjectDoesNotExist:
#         raise Http404()

    
#     return render(request, 'prodview.html', {'product': product})
def one_image(request, myid):
    try:
        image = Product.objects.filter(id=myid)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'prodview.html', {'image': image})


def profile(request):
    return render(request,'profile.html')

def order(request):


    return render(request,'order.html')

