
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from MyRestApp import views as v

router=routers.DefaultRouter()
router.register('st',v.StudentOperations)

router.register('urlst',v.StudentURLOperations)

router.register('user',v.UserURLoperations)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('rest_framework.urls')),
    path('',include('MyRestApp.urls')),
    path('',include(router.urls)),
]
