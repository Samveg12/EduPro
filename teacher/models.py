from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField

class Belonging(models.Model):
    user = models.OneToOneField(User, related_name="belonging", related_query_name="belonging", null=True, blank=True,
                                on_delete=models.CASCADE)
    is_student= models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Others(models.Model):
    user = models.OneToOneField(User, related_name="othdetails", related_query_name="othdetails", null=True, blank=True,on_delete=models.CASCADE)
    address = models.TextField(max_length=250, blank=True)
    phonenumber = models.IntegerField(default=9898944123)
    college=models.TextField(max_length=250, blank=True)
    edu=models.TextField(max_length=250, blank=True)



    def __str__(self):
        return self.edu
class Timings(models.Model):
    time=models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.time)
class NewCourse(models.Model):
    user = models.OneToOneField(User, related_name="othdetail", related_query_name="othdetail", null=True, blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,blank=False)
    timings=models.ManyToManyField(Timings)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=250, blank=True)
    



