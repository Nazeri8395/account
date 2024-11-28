from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    
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
     
    def __str__(self):
        return self.user.first_name

