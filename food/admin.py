from cProfile import Profile
from django.contrib import admin
from .models import Profile,Orders,Product,OrderUpdate
# Register your models here.
admin.site.register(Profile)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(OrderUpdate)