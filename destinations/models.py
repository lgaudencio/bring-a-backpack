from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    """
    A model to create and manage all destination reviews
    """
    user = models.ForeignKey(User, related_name='destination_review_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    brief = models.CharField(max_length=450, null=False, blank=False)
