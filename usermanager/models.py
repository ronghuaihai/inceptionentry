from __future__ import unicode_literals

from django.db import models
from mysqldbmanager.models import Mysqldbinfo

# Create your models here.
class userRole(models.Model):
    userRole=models.CharField(max_length=15)
    def __unicode__(self):
        return u'%s'  %(self.userRole)



class generalUser(models.Model):
    generalUserName=models.CharField(max_length=50)
    generalUserPassword=models.CharField(max_length=50)
    generalUserMail=models.CharField(max_length=50)
    generalUserDatabase=models.ManyToManyField(Mysqldbinfo)
    generalUserRole=models.ManyToManyField(userRole)
    def __unicode__(self):
        return u'%s %s %s %s' % (self.generalUserName,self.generalUserMail,self.generalUserDatabase,self.generalUserRole)
