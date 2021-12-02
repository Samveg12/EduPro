from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.Student.login,name="loginpage"),
    path('/rated',views.Student.rate,name="rate")
    # path('login', views.loginpage, name="login")

]
