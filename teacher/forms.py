from django import forms
from django.db.models import fields
from teacher.models import Others,NewCourse
from django.contrib.auth.models import User

class Registerdetail(forms.ModelForm):
    class Meta:
        model=Others
        fields = "__all__"
        exclude = ('user',)

class newCourse(forms.ModelForm):
    class Meta:
        model=NewCourse
        fields="__all__"
        exclude=('user',)