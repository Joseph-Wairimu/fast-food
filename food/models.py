from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    delivery_time = models.IntegerField(default=0)
    min_order = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name   

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} ordered {self.food.name}'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food.name
