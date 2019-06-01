from django import forms
from .models import Sub

class SubForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ('origin', 'new')
        widgets = {
            'origin': forms.TextInput(
                attrs = {
                    'class': 'form-group',
                    'id': 'origin',
                    'placeholder': 'Your original URL here'
                }
            ),
            'new': forms.TextInput(
                attrs = {
                    'class': 'form-group',
                    'id': 'linked',
                    'maxlength': 30,
                    'placeholder': 'Your new linked URL here'
                }
            ),
        }