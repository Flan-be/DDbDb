from django.db import models

# Create your models here.

class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.name


class Orders(models.Model):
    orderID = models.AutoField(primary_key=True)
    order_content = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        app_label = 'core'

    def __str__(self):
        return f"Order {self.orderID}"


class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.name