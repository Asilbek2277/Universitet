from django import forms

from .models import *


#4-misol
class FanForm(forms.ModelForm):
    class Meta:
        model=Fan
        fields='__all__'

#5-misol
class YonalishForm(forms.ModelForm):
    class Meta:
        model=Yonalish
        fields='__all__'


#6-misol
class UstozForm(forms.ModelForm):
    class Meta:
        model=Ustoz
        fields='__all__'