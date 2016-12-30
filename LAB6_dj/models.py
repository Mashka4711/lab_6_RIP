from django.db import models

class ClientModel(models.Model):
    client_first_name = models.CharField(max_length=30)
    client_email = models.EmailField(max_length=80)
    client_phone = models.CharField(max_length=40)
    client_address = models.CharField(max_length=100)
    order_number = models.ForeignKey('OrderModel',null=True)


class ServiceModel (models.Model):
    service_price = models.CharField(max_length=20)
    service_type = models.CharField(max_length=40)
    service_class_of_price = models.CharField(max_length=20)


class OrderModel (models.Model):
    order_number = models.IntegerField(unique=True)
    order_data = models.DateField()
    service = models.ForeignKey('ClientModel',null=True)