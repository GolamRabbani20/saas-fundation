from django.db import models

class PageVisits(models.Model):
    path = models.TextField(blank=True, null=True)
    timestamp = models.TimeField(auto_now_add=True)
