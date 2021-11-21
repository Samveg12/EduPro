
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from bootstrap_datepicker_plus import DateTimePickerInput
from student.forms import Registerdetail
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from student.models import Belongs,otherDetails,Education
from teacher.models import Belonging

from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.

def loginpage(request):
    if request.method=="POST":
        #s=foodAvbl.objects.get(city=request.user.city)
        # now = timezone.now()
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            print("????????????")
            print(user)
            if(Belongs.objects.get(user = user) is not None):
                if Belongs.objects.get(user = user).is_student:
                    login(request,user)
                    # details=otherDetails.objects.filter(user=request.user).values_list('city')
                    # for d in details:
                    #     s=Cities.objects.get(pk=d[0])
                    # j=foodAvbl.objects.filter(city=s)
                    # for i in j:
                    #     if i.created_on != None:
                    #         i.created_on += timedelta(hours=i.edible)
                    #         print(i.created_on)
                    #         if now>i.created_on:
                    #             history = History(user=i.user,otherDetails=i.otherDetails,measurement=i.measurement,typee=i.typee,quantity=i.quantity,Other_Specifics=i.Other_Specifics,images=i.images,city=i.city,pickup_address=i.pickup_address,created_on=i.created_on,edible=i.edible)
                    #             history.save()
                    #             i.delete()
                    # h=orders.objects.all()
                    # print(h)
                    # parameter={'j':j,'h':h}
                    messages.success(request,"Successfully Logged in")
                    return HttpResponseRedirect('/student/')
            if(Belonging.objects.get(user = user) is not None):
                if Belonging.objects.get(user = user).is_teacher:
                    login(request,user)
                    # details=otherDetails.objects.filter(user=request.user).values_list('city')
                    # for d in details:
                    #     s=Cities.objects.get(pk=d[0])
                    # j=foodAvbl.objects.filter(city=s)
                    # for i in j:
                    #     if i.created_on != None:
                    #         i.created_on += timedelta(hours=i.edible)
                    #         print(i.created_on)
                    #         if now>i.created_on:
                    #             history = History(user=i.user,otherDetails=i.otherDetails,measurement=i.measurement,typee=i.typee,quantity=i.quantity,Other_Specifics=i.Other_Specifics,images=i.images,city=i.city,pickup_address=i.pickup_address,created_on=i.created_on,edible=i.edible)
                    #             history.save()
                    #             i.delete()
                    # h=orders.objects.all()
                    # print(h)
                    # parameter={'j':j,'h':h}
                    messages.success(request,"Successfully Logged in")
                    return HttpResponseRedirect('/teacher/')

            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'Login/login.html')
            

        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'Login/login.html')
    # if request.user.is_authenticated:
        # details=otherDetails.objects.filter(user=request.user).values_list('city')
        # for d in details:
        #     s=Cities.objects.get(pk=d[0])
        # j=foodAvbl.objects.filter(city=s)
        # h=orders.objects.all()
        # print(h)
        # now = timezone.now()
        # for i in j:
        #     if i.created_on != None:
        #         i.created_on += timedelta(hours=i.edible)
        #         if now>i.created_on:
        #             history = History(user=i.user,otherDetails=i.otherDetails,measurement=i.measurement,typee=i.typee,quantity=i.quantity,Other_Specifics=i.Other_Specifics,images=i.images,city=i.city,pickup_address=i.pickup_address,created_on=i.created_on,edible=i.edible)
        #             history.save()
        #             i.delete()
        # parameter={'j':j,'h':h}
        # if(Belongs.objects.get(user = user).is_teacher):

        #     messages.success(request,"Successfully Logged in")
        #     return render(request,'Edupro/teacher/templates/teacher/index.html')
        # elif(Belongs.objects.get(user = request.user).is_student):
        #     messages.success(request,"Successfully Logged in")
        #     return render(request,'Edupro/student/templates/student/index.html')
        # else:
        #     return(HttpResponse("HELLLLLLLo"))
    else:
        print("Hii")
        messages.success(request, "You need to login to access this")
        return render(request, 'Login/login.html')
