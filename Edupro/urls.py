from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
    path('login/',include('Login.urls')),
    path('',TemplateView.as_view(template_name='student/final.html')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
