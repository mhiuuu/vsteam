from django.db import models
from tinymce.models import HTMLField
# Create your models here.

def default_img():
    return "static/assets/vietnamsteamunionlogo.jpg"

categories = [
    ("Programming and electronics", "Lập trình - Điện tử"),
    ("Mechanical and design", "Cơ khí - Thiết kế"),
    ("Business", "Quản lí - Tài chính"),
    ("Communication and Foreign Affairs", "Truyền thông - Đối ngoại"),
]

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=categories)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default=default_img, null=True)
    content = HTMLField()
    pubdate = models.DateField()
    update_date = models.DateField(null=True, blank=True)
    editors = models.CharField(max_length=255, null=True, blank=True) 
    author = models.CharField(max_length=255)
    #views = models.PositiveBigIntegerField()

