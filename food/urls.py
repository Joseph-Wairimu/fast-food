from django.urls import path,register_converter,include
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   


]