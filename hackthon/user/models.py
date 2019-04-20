from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    nickName = models.CharField(max_length=30)
    avatarUrl = models.CharField(max_length=100)
    gender = models.CharField(max_length=2 , choices=((u'M',u'Male'),(u'F',u'Female')))
    openId = models.CharField(max_length=30)

