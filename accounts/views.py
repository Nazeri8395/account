# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action

# from accounts.permissions import SendPrivateEmailToCustomerPermission
# from .models import Customer
# from .serializers import CustomerSerializer
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from rest_framework.permissions import AllowAny,DjangoModelPermissions

# # {
# #     "username": "eiliya",
# #     "password": "narges#1383"
# # }
# # {
# #     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMjkxMDMxNSwiaWF0IjoxNzMyODIzOTE1LCJqdGkiOiJlMzc5N2E0NzlkMDc0MzI3YWY5MWNhYzAzZjk5OWIzOCIsInVzZXJfaWQiOjR9.nrY22jm54qJ35E_h2XIZfdzkD-LaCaGHXdK4BbRTHTU",
# #     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxNDYzOTE1LCJpYXQiOjE3MzI4MjM5MTUsImp0aSI6ImE3Y2Q3ZDVmODEzMDQyYjRhMjRlZTQ4OWEzNWEzNjg5IiwidXNlcl9pZCI6NH0.RzUh_9JnMOL-_3_xUgIEJhaRwQHt8PZvIo-NyVu9jL4"
# # }
# class CustomerViewSet(ModelViewSet):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()
#     # permission_classes = [IsAdminUser]
    
#     @action(detail=False, methods=['GET', 'PUT'])
#     def me(self, request):
#         user_id = request.user.id
#         customer = Customer.objects.get(user_id=user_id)
#         if request.method == 'GET':
#             serializer = CustomerSerializer(customer)
#             return Response(serializer.data)
#         elif request.method == 'POST':
#             serializer = CustomerSerializer(customer, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)

#     @action(detail=True, permission_classes= [SendPrivateEmailToCustomerPermission])
#     def send_private_email(self, request, pk):
#         return Response(f'Sending email to customer {pk=}')







from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
