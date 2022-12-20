from django.db import models
from users.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    done_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)

class Service(models.Model):
    name = models.CharField(max_length=80,unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to="apipagos/images")
    
class Payment(models.Model):
    user_id = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service,null=True,blank=True,on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    paymentdate = models.DateField()
    expirationdate = models.DateField()

class ExpiredPayments(models.Model):
    payment_user_id = models.ForeignKey(Payment,null=True,blank=True,on_delete=models.CASCADE)
    penalty_fee = models.FloatField(default=0.0)