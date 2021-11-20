from django.db import models
from django.contrib.auth.models import User

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



    def __str__(self):
        return self.college
