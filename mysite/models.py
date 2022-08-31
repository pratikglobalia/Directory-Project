from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Directory(models.Model):
    name = models.CharField(max_length=100)
    directory = models.ForeignKey('self', on_delete=models.CASCADE, related_name='self1', null=True, blank=True)
    
    def __str__(self):
        return self.name

    
class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, null=True, blank=True)