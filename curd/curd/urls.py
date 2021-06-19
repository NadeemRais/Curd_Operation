"""curd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from curdapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home',views.home, name='home'),
    path('addstudent/',views.AddStudent, name='addstudent'),
    path('update/<pk>', views.update_form, name='update'),
    path('save_update/<pk>',views.saveUpdate, name='save_update'),
    path('delete/<pk>',views.deleteStudent, name='delete'),
    path('login/',views.loginPage, name='login'),
    path('login_student/',views.loginStudent, name='login_student')

]
