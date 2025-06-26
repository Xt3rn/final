from django import forms
from .models import Diplom

class DiplomForm(forms.ModelForm):
    class Meta:
        model = Diplom
        fields = ['student_name', 'title', 'supervisor', 'year', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }