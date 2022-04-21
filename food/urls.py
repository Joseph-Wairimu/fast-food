from django.urls import path,register_converter,include
from . import views

urlpatterns = [
   path('',views.index,name='index'),

   path('products/', views.products, name='products'),
   


   path('food/menu',views.menu,name='menu')


]