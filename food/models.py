

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.
#profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    image = CloudinaryField('image')
    desc = models.CharField(max_length=500, default="")
    
    post_date = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.user.username  
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()  

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

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

