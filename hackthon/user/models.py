from django.db import models

# Create your models here.
class User(models.Model):
    nick_name = models.CharField(max_length=30)
    avatar_url = models.CharField(max_length=100)
    gender = models.CharField(max_length=2 , choices=((u'M',u'Male'),(u'F',u'Female')))
    open_id = models.CharField(max_length=30)

