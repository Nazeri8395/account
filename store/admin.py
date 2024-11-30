from django.contrib import admin

from store.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',]
    list_per_page = 10
    ordering = ['user__last_name', 'user__first_name',]
    search_fields = ['user__last_name__istartswith', 'user__first_name__istartswith',]
    
    # def first_name(self, customer):
    #      return customer.user.first_name

    # def last_name(self, customer):
    #      return customer.user.last_name
   
    # def email(self, customer):
    #      return customer.user.email
     
     