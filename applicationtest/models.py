from django.db import models

# Create your models here.
class Newuser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return u'%s' % self.username
