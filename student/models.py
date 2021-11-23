from time import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
from teacher.models import NewCourse
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from datetime import timedelta
import datetime


class Belongs(models.Model):
    user = models.OneToOneField(User, related_name="belong", related_query_name="belong", null=True, blank=True,
                                on_delete=models.CASCADE)
    is_student= models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Education(models.Model):
    degree = models.CharField(max_length=100, default="enter")
    def __str__(self):
        return self.degree
# Create your models here.

class otherDetails(models.Model):
    user = models.OneToOneField(User, related_name="details", related_query_name="details", null=True, blank=True,on_delete=models.CASCADE)
    address = models.TextField(max_length=250, blank=True)
    phonenumber = models.IntegerField(default=9898944123)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, null=True)
    college=models.TextField(max_length=250, blank=True)
class FixTimings(models.Model):
    time = models.TimeField(null=True, blank=True, default=None)
    def __str__(self):
        return str(self.time)
class myBookedSlots(models.Model):
    def validate_date(date):
        if datetime.datetime.now().date()<=date<=datetime.datetime.now().date() + timedelta(days=3):
            return(True)
        else:
            raise ValidationError("Date has to be within current date and 3 days after current date")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booked_course=models.ForeignKey(NewCourse,on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, default=None, validators=[validate_date])
    time=models.OneToOneField(FixTimings, related_name="belongss", related_query_name="belongss", null=False, blank=False,
                                on_delete=models.CASCADE)
    

class Review(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    course=models.ForeignKey(NewCourse,on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=20,blank=False)
    score=models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    desc=models.TextField(max_length=250, blank=True)




    # teacher=models.ForeignKey(User,on_delete=models.CASCADE)




    
