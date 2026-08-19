from django import forms
from .models import Expences

class ExpencesForm(forms.ModelForm):
    class Meta :
        model = Expences
        fields = ('title','amount','category')

