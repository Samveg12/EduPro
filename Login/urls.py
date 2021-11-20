from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.loginpage,name="loginpage"),
    # path('login', views.loginpage, name="login")

]
