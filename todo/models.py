from django.db import models

# Create your models here.

# reset id by command: <python manage.py sqlsequencereset>
class Task(models.Model):
    content = models.CharField(max_length=100, blank=True)
    tomato = models.CharField(max_length=100, blank=True)
    finished = models.BooleanField(default=False, blank=False)

class TimeLine(models.Model):
    # time = models.CharField(max_length=20)
    content = models.TextField(default="TimeLine is Empty..")

