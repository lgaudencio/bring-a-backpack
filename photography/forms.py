from django import forms
from .models import Photography


class PhotographyForm(forms.ModelForm):
    """
    Form used to create a photography post
    """
    class Meta:
        model = Photography
        fields = [
            'post_title',
            'post_brief',
            'main_photo',
            'main_photo_alt',
            'photo_1',
            'photo_1_alt',
            'photo_2',
            'photo_2_alt',
            'photo_3',
            'photo_3_alt',
            'photo_4',
            'photo_4_alt',
            'photo_5',
            'photo_5_alt',
            'photo_6',
            'photo_6_alt',
            'photo_7',
            'photo_7_alt',
            'photo_8',
            'photo_8_alt',
            'photo_9',
            'photo_9_alt'
        ]
        widget = {
            'post_brief': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'post_title': 'Photography Post Title',
            'post_brief': 'Brief Description of Post',
            'main_photo': 'Main Photo',
            'main_photo_alt': 'Description of Main Photo',
            'photo_1': 'Photo Post',
            'photo_1_alt': 'Description of the above photo post',
            'photo_2': 'Photo Post',
            'photo_2_alt': 'Description of the above photo post',
            'photo_3': 'Photo Post',
            'photo_3_alt': 'Description of the above photo post',
            'photo_4': 'Photo Post',
            'photo_4_alt': 'Description of the above photo post',
            'photo_5': 'Photo Post',
            'photo_5_alt': 'Description of the above photo post',
            'photo_6': 'Photo Post',
            'photo_6_alt': 'Description of the above photo post',
            'photo_7': 'Photo Post',
            'photo_7_alt': 'Description of the above photo post',
            'photo_8': 'Photo Post',
            'photo_8_alt': 'Description of the above photo post',
            'photo_9': 'Photo Post',
            'photo_9_alt': 'Description of the above photo post'
        }
