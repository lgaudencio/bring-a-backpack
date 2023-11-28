from django import forms
from .models import Profile 


class ProfileForm(forms.ModelForm):
    """ 
    Form used to create a profile
    """
    class Meta:
        model = Profile 
        fields = ["display_picture", "nationality", "traveler_type", "bio"]
        labels = {
            "display_picture": "Display Picture",
            "nationality": "Nationality",
            "traveler_type": "Type of Traveler",
            "bio": "Bio"
        }
        