
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import Registerdetail,newCourse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from .models import Belonging,Others,NewCourse
from student.models import Belongs
from django.core.mail import send_mail
from django.utils import timezone

def index(request):
    return render(request,'teacher/index.html')

def signup(request):
    if request.method == "POST":
        
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists try with a new one !")
            return redirect('/teacher/signup')
        if (len(username) < 2 or len(username) > 20):
            messages.error(request, "Username doesnt match the requirements")
            return redirect('/teacher/signup')
        if (password != password1):
            messages.error(request, "Both passwords dont match")
            return redirect('/teacher/signup')
        myuser = User.objects.create_user(username, email, password)
        belong = Belonging(user=myuser, is_teacher=True)
        u = Belongs(user=myuser)
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
        return render(request, 'teacher/signup.html', {"form": form})
def logout_u(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect("/login")
# @login_required

# def checkk(request):
#     m=request.user
#     if Belonging.objects.get(user = m) is not None:
#         if(Belonging.objects.get(user = m).is_teacher):
#             return(True)
#         else:
#             return(False)


def newcourse(request):
    userr=request.user
    m=str(request.user)
    print("****")
    print(userr)
    if(m is not 'AnonymousUser'):
        if(Belongs.objects.get(user = userr).is_student is False):
            if(request.method == "POST"):
                # title=request.POST.get('title')
                # timings=request.POST.get('timings')
                # price=request.POST.get('price')
                # description=request.POST.get('description')
                form = newCourse(request.POST, request.FILES)
                if form.is_valid():
                    object = form.save(commit=False)
                    object.user = request.user
                    print("::::::::")
                    print(object.user)
                    object.save()
                    # object.save_m2m()
                return HttpResponse("FORM SUCCESSFULLY SAVED")
            else:
                form = newCourse()
                return render(request, 'teacher/newcourse.html', {"form": form})
        else:
            return redirect("/teacher/logout")

    else:
        return redirect("/login")






