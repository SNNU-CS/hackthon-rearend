from django.db import models


# Create your models here.
class UserActivity(models.Model):
    user_id = models.IntegerField()
    activity_id = models.IntegerField()
    user_class = models.TextField(choices=((u'S', u'发起者'), (u'A', u'参与者')))
