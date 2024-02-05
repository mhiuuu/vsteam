from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Services(models.Model):
    serviceName = models.CharField(max_length=50)
    serviceDesc = models.CharField(max_length=255)
    serviceImg = models.ImageField(upload_to="images/")


class Achievements(models.Model):
    achieve = models.CharField(max_length=50)
    achieveDesc = models.CharField(max_length=255)

class About(models.Model):
    Intro = HTMLField()