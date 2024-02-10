"""
URL configuration for student_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from student_application.views import TableView, UserLogin, save_register_page, Save_Student_Info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Save_Student_Info/', Save_Student_Info.as_view(), name='Save_Student_Info'),
    path('table/', TableView.as_view(), name='table_view'),
    path('save_register_page/', save_register_page.as_view(), name='save_register_page'),
    path('UserLogin/',UserLogin.as_view(), name='save_login_page'),
]
