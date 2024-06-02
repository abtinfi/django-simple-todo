from django.db import models
#python manage.py makemigration
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField()
    
    