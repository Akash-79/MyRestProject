from django.db import models

class Emp(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)

    def __str__(s):
        return s.Name

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=20)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=30)
    Address=models.CharField(max_length=300)
    Email=models.CharField(max_length=30)


from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'

class MyForm(forms.Form):
    name=forms.CharField(max_length=30)
    address=forms.CharField(max_length=60)
    date=forms.DateField()
    age=forms.IntegerField()

class DataForm(forms.Form):
    name=forms.CharField(max_length=30,label="Enter Name")
    email=forms.EmailField(max_length=30,help_text="Enter Email With Domain")
    address=forms.CharField(widget=forms.Textarea)
    date=forms.DateField(widget=forms.SelectDateWidget)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
