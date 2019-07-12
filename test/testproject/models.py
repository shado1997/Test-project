from django.db import models
from datetime import datetime
from django.utils import timezone

class Groups(models.Model):
    """
    Model representing lists of users.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

LIST_OF_GROUPS = Groups.objects.values_list('id', 'name')

class Users(models.Model):
    """
    Model representing lists of users.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    created = models.DateField(default=timezone.now())
    group = models.ForeignKey('Groups', on_delete=models.CASCADE, choices=LIST_OF_GROUPS)
    
    def __int__(self):
        return self.id







