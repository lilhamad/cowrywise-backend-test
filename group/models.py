from django.db import models

class Group(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    weekly_amount = models.IntegerField()
    capacity = models.IntegerField()
    searchable = models.BooleanField(default=True)
    
    