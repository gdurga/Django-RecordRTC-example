from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Audiofl(models.Model):
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    fl = models.FileField(
        upload_to='audio_uploads',
        blank=True,
        null=True,
        verbose_name=u'File')
