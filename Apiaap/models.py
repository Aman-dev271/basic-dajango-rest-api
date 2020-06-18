from django.db import models

# Create your models here.
class student(models.Model):
    s_name = models.CharField(max_length=20)
    s_ph = models.IntegerField()
    s_email = models.EmailField()
    s_img = models.ImageField(default=0)

