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



@login_required(login_url='login') 
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

@login_required(login_url='login') 
def one_image(request, myid):
    try:
        image = Product.objects.filter(id=myid)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'prodview.html', {'image': image})


@login_required(login_url='login') 
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
   
    context = {'profile':profile}
    return render(request,'profile.html',context)

@login_required(login_url='login') 
def update_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            data = form.cleaned_data
            profile.user = current_user
            profile.name = data['name']          
            profile.phone = data['phone']
            profile.image = data['image']
            profile.save()
            return redirect('/profile')
    else:
        form = ProfileForm()
    return render(request, 'update.html', {'form': form})



    
@login_required(login_url='login') 
def checkout(request):
    current_user = request.user
    form = OrdersForm(request.POST, request.FILES)
    if request.method == 'POST':   
        if form.is_valid():
            bst = form.save(commit=False)
            bst.user = request.user
            bst.neighbourhood = hood
            bst.save()
            return redirect ('products')
        else:
            form = OrdersForm()
    return render(request,'checkout.html',{ 'form':form})

# def checkout(request):
#     if request.method == "POST":
#         items_json = request.POST.get('itemsJson', '')
#         user_id = request.POST.get('user_id', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amount', '')
#         email = request.POST.get('email', '')
#         address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')
#         order = Orders(items_json=items_json, userId=user_id, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
#         order.save()
#         update = OrderUpdate(order_id=order.order_id, update_desc="The Order has been Placed")
#         update.save()
#         thank = True
#         id = order.order_id
#         if 'onlinePay' in request.POST:
#             # Request paytm to transfer the amount to your account after payment by user
#             darshan_dict = {

#                 'MID': 'WorldP64425807474247',  # Your-Merchant-Id-Here
#                 'ORDER_ID': str(order.order_id),
#                 'TXN_AMOUNT': str(amount),
#                 'CUST_ID': email,
#                 'INDUSTRY_TYPE_ID': 'Retail',
#                 'WEBSITE': 'WEBSTAGING',
#                 'CHANNEL_ID': 'WEB',
#                 'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

#             }
 
        
#             return render(request, 'checkout.html', {'thank': thank, 'id': id})
#     return render(request, 'checkout.html')


