from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        permissions = [
                ('send_private_email', 'Can send private email to user by the button')   
        ]
    @property
    def  first_name(self):
    	return  self.user.first_name
 
    @property
    def  last_name(self):
    	return   self.user.last_name
    
    @property
    def  email(self):
    	return   self.user.email
 
    @property
    def  full_name(self):
    	return  f'{self.user.first_name} {self.user.last_name}'
 
class Address(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
