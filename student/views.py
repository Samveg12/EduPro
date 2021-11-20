
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import Registerdetail
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from .models import Belongs,otherDetails,Education
from teacher.models import  Belonging
from django.core.mail import send_mail
from django.utils import timezone
# Create your views here.

def index(request):
    

    return render(request,'teacher/index.html',{})

# def Email(username,email):
#     send_mail(
#         subject = "alert",
#         message = f'thanks {username} for joining us. Your account has been successfully created login for more details',
#         from_email = "samvegvshah13@gmail.com",
#         recipient_list = [email],
#         fail_silently = False,
#     )


def signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists try with a new one !")
            return redirect('/student/signup')
        if (len(username) < 2 or len(username) > 20):
            messages.error(request, "Username doesnt match the requirements")
            return redirect('/student/signup')
        if (password != password1):
            messages.error(request, "Both passwords dont match")
            return redirect('/student/signup')
        myuser = User.objects.create_user(username, email, password)
        belong = Belongs(user=myuser, is_student=True)
        u=Belonging(user=myuser)
        u.save()
        belong.save()
        myuser.save()
        
        # Email(username,email)
        form = Registerdetail(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = myuser
            object.save()

        messages.success(request, "Your NGO account has been successfully created")
        return HttpResponse("SUCCESS")

    else:
        form = Registerdetail()
        return render(request, 'student/signup.html', {"form": form})
