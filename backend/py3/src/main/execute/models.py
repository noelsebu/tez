from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Testcases(models.Model):
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Family.
        """
        return reverse('family-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.title
    #testscript=models.TextField()
    selected=models.ForeignKey('Selected',on_delete=models.PROTECT)
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.testid
class Selected(models.Model):

    team_name = models.TextField()
    testid = models.TextField()
    automatable_reason=models.TextField()
    testscript=models.TextField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Family.
        """
        return reverse('selected-detail-view', args=[str(self.id)])

    def __str__(self):

        return self.testid
    

