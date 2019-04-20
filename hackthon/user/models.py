from django.db import models


# Create your models here.
class User(models.Model):
    nick_name = models.CharField(max_length=30)
    avatar_url = models.CharField(max_length=100)
    gender = models.CharField(choices=((u'M', u'男'), (u'F', u'女'), (u'U',
                                                                    u'未知')))
    open_id = models.CharField(max_length=30)
