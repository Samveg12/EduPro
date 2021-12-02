
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import Registerdetail,Reviewz,MyBookeds
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from .models import Belongs,otherDetails,Education,myBookedSlots,Review
from teacher.models import  Belonging,NewCourse
from django.core.mail import send_mail
from django.utils import timezone
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
# Create your views here.

@login_required
def index(request):
    f=NewCourse.objects.all()
    print("====")
    print(f)
    parameter={'f':f}



    return render(request,'student/index.html',parameter)


# def Email(username,email):
#     send_mail(
#         subject = "alert",
#         message = f'thanks {username} for joining us. Your account has been successfully created login for more details',
#         from_email = "samvegvshah13@gmail.com",
#         recipient_list = [email],
#         fail_silently = False,
#     )

def logout_u(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect("/login")




razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payu.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,id):
 
    # only accept POST request.
    if request.method == "POST":
        try:
              
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            # print(")))))))")
            print(payment_id)
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)

            if result is None:

                amount = 20000  # Rs. 200
                try:
                    print("HEYy")
                    print(payment_id)
                    print(amount)
                    s=myBookedSlots.objects.last()
                    print(s)
                    semail=request.user.email
                    temail=s.booked_course.user.email
                    print(semail)
                    print(temail)
                    meet(s.date,s.time,semail,temail)
                    # capture the payemt
                    # razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    #student (my booked slots)
                    #teacher(my booked slots)
                    
                    



                    return HttpResponse("Payment SUCCESS")
                except:
                    print("------")
 
                    # if there is an error while capturing payment.
                    return HttpResponse("Payment FAILED")
            else:
                print("----------------------------")
                # if signature verification fails.
                return HttpResponse("Payment FAILED")
        except:
            # print("EHEHEHEHE")
            # if we don't find the required parameters in POST data
            Payment.confirmation()
            Payment.displayDetails()
            Payment.pay()
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
        
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

class Revieww:
    def isLectureTaken(j):
        j=True
        return(j)
    def updatereview(request,id):
        form = MyBookeds(request.POST, request.FILES)
        return HttpResponse("Hello")
    def updaterating(request,id):
        rate=id
        
        studentId=NewCourse.objects.filter(id=id)[0]
        teacherId=NewCourse.objects.filter(id=id)[0]
        review=Review.objects.all()
        lectureTaken=False
        m=Revieww.isLectureTaken(lectureTaken)
        if(request.method=="POST"):
            form = MyBookeds(request.POST, request.FILES)
                # date=request.POST.get('date')
                # print(date)
                # y=NewCourse.objects.filter(id=id)[0]
                # u=myBookedSlots.objects.create(user=request.user,booked_course=y,datee=date)
            print("&*&*&*&*&*")
            print(form)    
            if form.is_valid():
                print("______---")

                object = form.save(commit=False)
                object.user = request.user
                    
                object.booked_course=NewCourse.objects.filter(id=id)[0]
                object.save() 
                u=object.id
            print(";;;;")

            y=NewCourse.objects.filter(id=id)

            currency = 'INR'
            amount = str(y[0].price*100)  # Rs. 200
        
            # Create a Razorpay Order
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                            currency=currency,
                                                            payment_capture='0'))
        
            # order id of newly created order.
            razorpay_order_id = razorpay_order['id']
            callback_url = 'paymenthandler/'+str(id)
        
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
            context['y']=y[0]
            u=Review.objects.all()
            k=[]
            m=[]
            flag=0
            for i in u:
                if(i.course.id==id):
                    # k.append(i)
                    if(i.user==request.user):
                        flag=1
                        k.append(i)
            for i in u:
                if(i.course.id==id):
                    if(i.user==request.user):
                        continue
                    else:
                        k.append(i)
            if(flag):
                d=k[0]
                k.pop(0)
                context['d']=d
                print(d.id)
            form = MyBookeds()
            context['form']=form
            context['k']=k
            context['flag']=flag
            context['u']=u
        


    
            return render(request, 'student/details.html', context=context)
        else:
            
            return HttpResponse("HELLo")
def bookings(request):
    s=myBookedSlots.objects.filter(user=request.user)
    context={'s':s}
    return render(request, 'student/myslots.html', context)

class Payment:
    def displayDetails(request):

        paymentid = request.POST.get('razorpay_payment_id', '')
        amount = request.POST.get('razorpay_amount_id', '')
        confirm = True
            # print(")))))))")
        params_dict = {
                'razorpay_order_id': amount,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': confirm
            }
        return HttpResponse("Payment success")
    
    def confirmation(request):
        s=myBookedSlots.objects.filter(user=request.user)
        context={'s':s}
        return render(request, 'student/myslots.html', context)


    def pay(request):
        return(True)




def createReview(request,id):
    if request.method == "POST":
        u=Review.objects.all()
        o=NewCourse.objects.filter(id=id)
        flag=0
        for i in u:
            if(i.user==request.user and i.course==o[0].id):
                flag=1
        if(flag==1):
            return HttpResponse("NOT ALLOWED")
        else:

        
            form = Reviewz(request.POST, request.FILES)
            if form.is_valid():
                object = form.save(commit=False)
                object.user = request.user
                object.course=NewCourse.objects.filter(id=id)[0]
                object.save()

            messages.success(request, "Your NGO account has been successfully created")
        return HttpResponse("SUCCESS")
        # print("hi")

    else:
        flag=0
        y=myBookedSlots.objects.all()
        print(y)
        for i in y:
            if(i.booked_course.id==id and i.user==request.user):
                print("JKJKJKJKJKJK")
                flag=1
                break
            print("===")
            print(i.user)
            print(request.user)
            print(i.booked_course.id)
            print(id)
        if(flag):
            form = Reviewz()
            print(form)
            return render(request, 'student/createreview.html', {"form": form,"id":id})
        else:
            return HttpResponse("YOU ARE NOT ALLOWED")

def meet(date,time,semail,temail):
    print(date)
    print(time)
    scopes = ['https://www.googleapis.com/auth/calendar']
    d=str(date)
    t=str(time)
    
    credentials = pickle.load(open(r"C:\D\Ashish\Projects\EduPro\student\token2.pkl", "rb"))
    
    
    service = build("calendar", "v3", credentials=credentials)
    
    result = service.calendarList().list().execute()
    
    calendar_id = result['items'][0]['id']
    result = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()
    
    start_time = datetime(int(d[0:4]), int(d[5:7]), int(d[8:10]), int(t[0:2]), int(t[3:5], 0))
    end_time = start_time + timedelta(hours=1)
    
    timezone = 'Asia/Kolkata'

    event = {
        'summary': 'Discussion Project',
        'location': 'Mumbai',
        'description': 'SE Lab',
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'conferenceDataVersion': 1,
        'conferenceData': {
                'createRequest': {
                        "requestId": "RandomString",
                        'conferenceSolutionKey': {
                            'type': 'hangoutsMeet'
                        },
                        #  'status': {
                        # 'statusCode': "404"
                        #  }
                        }
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'attendees': [
            {'email': semail},
            {'email': temail},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
            'sendNotifications':True,
        }
    service.events().insert(calendarId=calendar_id, conferenceDataVersion=1, body=event).execute()
    
    return HttpResponse("SUCCESS")

class updates(LoginRequiredMixin,UpdateView):
	model = Review
	template_name = "student/updatereview.html"
	fields = ("title","score","desc")
	success_url = "/student"
	def get_form(self):
		form = super(updates,self).get_form()
		# form.fields['startdate'].widget = DateTimePickerInput()
		# form.fields['enddate'].widget = DateTimePickerInput()
		return form 

class deletes(LoginRequiredMixin,DeleteView):
	model = Review
	template_name = "student/deletereview.html"
	success_url = "/student"

def chooseslot(request,id):
    form=MyBookeds()
    context={}
    context['id']=id
    context['form']=form
    return render(request,'student/timings.html',context)







    



