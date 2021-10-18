
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Employee, Group, Item, Job, Ledger, Supplier, User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=65, min_length=8, write_only=True)
   

    class Meta:
        model = User
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'

class LedgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ledger
        fields = '__all__'


         
            
  


# class UserSerializer(serializers.ModelSerializer):
#      password = serializers.CharField(max_length=65, min_length=8, write_only=True,)
#     mobile= serializers.CharField(max_length=12, min_length=10),
#     #username = serializers.CharField(max_length=15, min_length=2)
    
#     class Meta:
#         model = User
#         fields = ['username', 'mobile', 'password'
#                   ]

#     def validate(self, attrs):
#         mobile= attrs.get('mobile', '')
#         username= attrs.get('username', '')
#         password= attrs.get('password', '')
#         if User.objects.filter(username=username).exists():
#             raise serializers.ValidationError(
#                 {'username': ('username is already in use')})
#         if User.objects.filter(mobile=mobile).exists():
#             raise serializers.ValidationError(
#                 {'mobile': ('Mobile is already in use')})
#         if User.objects.filter(password=password).exists():
#             raise serializers.ValidationError(
#                 {'password': ('Password is already in use, Choice another one')})
       
#         return super().validate(attrs)
        

        

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)



# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=65, min_length=8, write_only=True)
#     username = serializers.CharField(max_length=255, min_length=2)

#     class Meta:
#         model = User
#         fields = ['username', 'password']










