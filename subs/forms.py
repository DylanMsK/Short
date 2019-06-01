from django import forms
from .models import Sub

class SubForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ('origin', 'new')
        labels = {
            'new': 'New Alias'
        }
        widgets = {
            'origin': forms.Textarea(
                attrs = {
                    'class': 'form-group',
                    'id': 'origin',
                    'cols': 80,
                    'rows': 3,
                    'placeholder': 'Your original URL here'
                }
            ),
            'new': forms.TextInput(
                attrs = {
                    'class': 'form-group',
                    'id': 'linked',
                    'maxlength': 30,
                    'placeholder': 'Your new linked URL here (less 30 letters)'
                }
            ),
        }
        help_texts = {
            'new': 'http://url.diet/[linked url]'
        }