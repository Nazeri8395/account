# from rest_framework.response import Response

# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action
# from store.models import Customer
# from .serializers import CustomerSerializer
# # from rest_framework.permissions import IsAdminUser, IsAuthenticated


# class CustomerViewSet(ModelViewSet):
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()
#     # permission_classes = [IsAdminUser]
    
#     @action(detail=False, methods=['GET', 'PUT'])
#     def me(self, request):
#         user_id = request.user.id
#         print(request.user.id)
#         customer = Customer.objects.get(user__id=user_id)
#         if request.method == 'GET':
#             serializer = CustomerSerializer(customer)
#             return Response(serializer.data)
#         elif request.method == 'PUT' :
#             serializer = CustomerSerializer(customer, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         return Response("you dont")

  
