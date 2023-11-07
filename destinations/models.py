from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField 

class Destination(models.Model):
    """
    A model to create and manage all destination reviews
    """
    user = models.ForeignKey(User, related_name='destination_review_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    brief = models.CharField(max_length=450, null=False, blank=False)
    photo = ResizedImageField(
        size=[500, None], quality=75, upload_to='destinations/', force_format='WEBP', null=False,
        blank=False
    )
    photo_alt = models.CharField(max_length=100, null=False, blank=False)
    review = RichTextField(max_length=20000, null=False, blank=False)
