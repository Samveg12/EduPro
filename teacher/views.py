
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import Registerdetail,newCourse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from .models import Belonging,Others,NewCourse
from student.models import Belongs,myBookedSlots
from django.core.mail import send_mail
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


def index(request):
    s=NewCourse.objects.filter(user=request.user)
    paramter={'s':s}
    return render(request,'teacher/index.html',paramter)

# AI-2
# TOC-4
# OOPS-2
# SE-2
# DC-1


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
class Slot:

    def bookSlot(request):
        s=myBookedSlots.objects.all()
        bookingid=s[0].id
        studentid=s[0].user
        datetime=timezone.now()
        print("======ghjhjhjhjh")
        print(studentid)
        print(datetime)
        v=[]
        for i in s:
            if(i.user==request.user):
                v.append(i)
        return render(request, 'teacher/booked.html', {'v':v})
    def checkTeacherAvaible(request):
        return HttpResponse("Avaible")





class Teacher:

    def updateCourses(request):
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
                updateSubjects()
                return redirect("/teacher/logout")

        else:
            return redirect("/login")
    def updateSubjects(request):
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
                        teacherid=object.id
                        subjects=object.title
                        courses=object.description
                        rating=object.timings
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
    def viewCalender(request):
        return HttpResponse("Calender")
class updates(LoginRequiredMixin,UpdateView):
	model = NewCourse
	template_name = "teacher/update.html"
	fields = ("title","timings","price","description")
	success_url = "/teacher"
	def get_form(self):
		form = super(updates,self).get_form()
		# form.fields['startdate'].widget = DateTimePickerInput()
		# form.fields['enddate'].widget = DateTimePickerInput()
		return form 

class deletes(LoginRequiredMixin,DeleteView):
	model = NewCourse
	template_name = "teacher/delete.html"
	success_url = "/teacher"




