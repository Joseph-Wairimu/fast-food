from django.urls import path,register_converter,include
from . import views

urlpatterns = [
   path('',views.index,name='index'),

   path('checkout/', views.checkout, name="checkout"),

   path('products/', views.products, name='products'),
   
   path('imagedetails/<myid>', views.one_image, name='imagedetails'),
   path('food/menu',views.menu,name='menu'),


   path('food/menu',views.menu,name='menu'),
   path('food/services',views.services,name='services'),
   path('food/about',views.about_us,name='about'),
   path('accounts/profile/',views.profile,name='profile'),


]