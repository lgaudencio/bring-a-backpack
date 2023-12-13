from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Photography(models.Model):
    """
    This is a model to create and manage the photography posts 
    """
    user = models.ForeignKey(User, related_name='photography_owner', on_delete=models.CASCADE)
    post_title = models.CharField(max_length=250, null=False, blank=False)
    post_brief = models.CharField(max_length=450, null=False, blank=False)
    main_photo = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    main_photo_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_1 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_1_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_2 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_2_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_3 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_3_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_4 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_4_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_5 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_5_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_6 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_6_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_7 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_7_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_8 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_8_alt = models.CharField(max_length=100, null=False, blank=False)
    photo_9 = ResizedImageField(
        size=[500, None], quality=75, upload_to='photography/', force_format='WEBP', null=False,
        blank=False
    )
    photo_9_alt = models.CharField(max_length=100, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.post_title)
    
