from django.db import models


# Create your models here.
class User(models.Model):
    nick_name = models.TextField()
    avatar_url = models.TextField()
    gender = models.TextField(default='M',
                              choices=((u'M', u'男'), (u'F', u'女'), (u'U',
                                                                    u'未知')))
    open_id = models.TextField()
