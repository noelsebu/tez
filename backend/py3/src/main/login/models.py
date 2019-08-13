from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Credentials(models.Model):
    username=models.TextField()
    password=models.TextField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Family.
        """
        return reverse('selected-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.username