from django.db import models


# Create your models here.
class UserActivity(models.Model):
    user_id = models.IntegerField()
    activity_id = models.IntegerField()
    user_class = models.TextField(choices=((u'S', u'发起者'), (u'A', u'参与者')))


class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time = models.DateTimeField()
    location = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    delete_time = models.DateTimeField(null=True, default=None)
