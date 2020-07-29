from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('',v.home ),
    path('addEmp',v.CreateEmp.as_view()),
    path('empList',v.EmpList.as_view()),
    path('cl',v.CreateEmpListView.as_view()),
    path('getEmp/<int:pk>',v.GetEmpView.as_view()),
    path('updateEmp/<int:pk>',v.UpdateEmpView.as_view()),
    path('deleteEmp/<int:pk>',v.DeleteEmpView.as_view()),
    path('udemp/<int:pk>',v.UpdateDeleteEmpView.as_view()),


    path('addAccount',v.CreateAccountListView.as_view()),

    path('addStudent',v.CreateStudent.as_view()),
    path('studentList/',v.StudentList.as_view()),
    path('sl/',v.CreateStudentListView.as_view()),

    #path('st',v.StudentOperations.as_view()),
    
]