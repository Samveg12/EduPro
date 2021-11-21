from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="student"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout_u, name="logout_u"),
    path('product/<int:id>', views.details, name="details"),
    path('payment',views.paymenthandler,name="paymenthandler")



    
]