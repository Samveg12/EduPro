from django import forms
from django.forms import fields
from django.forms.widgets import DateInput
from student.models import otherDetails,Review,myBookedSlots
from django.contrib.auth.models import User
from django.forms import ModelForm


class Registerdetail(forms.ModelForm):
    class Meta:
        model=otherDetails
        fields = "__all__"
        exclude = ('user',)

class Reviewz(forms.ModelForm):
    class Meta:
        model=Review
        fields = "__all__"
        exclude = ('user','course')

class MyBookeds(forms.ModelForm):
    class Meta:
        model=myBookedSlots
        fields=['date','time']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

