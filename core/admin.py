from django.contrib import admin
from .models import Customer, Orders, Product


# Register your models here.
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Product)