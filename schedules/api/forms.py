from django import forms
from matplotlib import widgets
from .models import mSchadules

class fSchedules(forms.ModelForm):
    class Meta:
        model = mSchadules
        fields = "__all__"
        widgets = {
            'schedule_name': forms.TextInput(attrs={'class':'form-control'}),
            'schedule_time': forms.TextInput(attrs={'class':'form-control'}),
        }