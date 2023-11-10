from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Destination


class DestinationForm(forms.ModelForm):
    """
    Form used to create a destination review
    """
    class Meta:
        model = Destination
        fields = ['title', 'brief', 'photo', 'photo_alt', 'review']
        review = forms.CharField(widget=RichTextWidget())
        widget = {
            'brief': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Review Title', 
            'brief': 'Brief Review Description',
            'photo': 'Review Photo', 
            'photo_alt': 'Describe Review Photo', 
            'review': 'Full Review'
        }
