"""exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path,include

from mainpage.views import main_page, hello_world, hello_personalized, sum_no, sub_no, mul_no
from maths.views import math_operations, math_list, math_details
from products.views import products_list, prodcuts_wypisz

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main_page),
    path("hello",hello_world),
    path("hello/<name>",hello_personalized),
    path("add/<no1>/<no2>",sum_no),
    path("sub/<no1>/<no2>",sub_no),
    path("mul/<no1>/<no2>",mul_no),
    path("maths",math_list),
    path("maths/<int:id>",math_details),
    path("maths/<operation>/<int:arg_a>/<int:arg_b>",math_operations),
    path("products/<nazwa>/<opis>/<int:cena>/<status>",products_list),
    path("products",prodcuts_wypisz),
]

urlpatterns += [
    path('accounts/',include('django.contrib.auth.urls'))
]