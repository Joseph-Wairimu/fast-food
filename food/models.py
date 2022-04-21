

from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.
#profile model
class Profile(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    image = CloudinaryField('image')
    desc = models.CharField(max_length=500, default="")
    
    post_date = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.user   

#place order class
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    userId = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userId 

#products/foods model

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.product_name


#order update class
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.update_desc

