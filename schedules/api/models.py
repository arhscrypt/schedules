from django.db import models

# Create your models here.
class mSchadules(models.Model):
    schedule_name = models.CharField(max_length=50)
    schedule_time = models.CharField(max_length=50)