from django.db import models

# Create your models here.
class UserActivity(models.Model):
    user_id = models.CharField(max_length=255)
    activity_id = models.CharField(max_length=255)
    user_class = models.CharField(max_length=2,choices=((u'S',u'Sponsor'),(u'A'),(u'Actor')))