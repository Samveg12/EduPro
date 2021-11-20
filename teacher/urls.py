from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="teachers"),
    path('signup', views.signup,name="signup"),
    path('newcourse',views.newcourse,name="newcourse"),
    path('logout',views.logout_u,name="logout_u")

    
]