from django import forms
from student.models import otherDetails
from django.contrib.auth.models import User

class Registerdetail(forms.ModelForm):
    class Meta:
        model=otherDetails
        fields = "__all__"
        exclude = ('user',)