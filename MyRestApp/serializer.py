from rest_framework import serializers
from .models import Emp,Account,Student

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class StudentURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','username','first_name','last_name','email']

    

