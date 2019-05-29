from django import forms
from .models import Sub

class SubForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = '__all__'