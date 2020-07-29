from django.shortcuts import render,HttpResponse
from rest_framework import generics,viewsets
from .models import Emp,Account,Student,EmpForm,MyForm,DataForm
from .serializer import EmpSerializer,AccountSerializer,StudentSerializer,UserSerializer

def home(request):
    f=EmpForm
    mf=MyForm
    df=DataForm
    d={'form':f,'mf':mf,'df':df}
    #return HttpResponse("<h1>Welcome Rest Api </h1>")
    return render(request,'index.html',d)


class CreateEmp(generics.CreateAPIView):
    serializer_class=EmpSerializer

class EmpList(generics.ListAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class CreateEmpListView(generics.ListCreateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class GetEmpView(generics.RetrieveAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class UpdateEmpView(generics.RetrieveUpdateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class DeleteEmpView(generics.RetrieveDestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class UpdateDeleteEmpView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class CreateAccountListView(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class StudentOperations(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

from . serializer import StudentURLSerializer
class StudentURLOperations(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentURLSerializer

from django.contrib.auth.models import User

class UserURLoperations(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer






class CreateStudent(generics.CreateAPIView):
    serializer_class=EmpSerializer

class StudentList(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class CreateStudentListView(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer






