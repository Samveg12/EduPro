from django.shortcuts import render
from django .http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
import datetime
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request,'student/index.html')
