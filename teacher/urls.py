from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="teachers"),
    path('signup', views.signup,name="signup"),
    path('newcourse',views.Teacher.updateCourses,name="updateCourses"),
    path('logout',views.logout_u,name="logout_u"),
    path('mybooked',views.Slot.bookSlot,name="mybooked"),
    path('teacheravaible',views.Slot.checkTeacherAvaible,name="mybooked"),
    path('update/<int:pk>',views.updates.as_view()),
    path('delete/<int:pk>',views.deletes.as_view()),  
]