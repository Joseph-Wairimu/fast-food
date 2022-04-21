from django.urls import path,register_converter,include
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('food/menu',views.menu,name='menu'),
   path('food/services',views.services,name='services'),

]