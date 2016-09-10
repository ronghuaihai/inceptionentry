from __future__ import unicode_literals

from django.db import models
from mysqldbmanager.models import Mysqldbinfo

# Create your models here.
class generalUser(models.Model):
    generalUserName=models.CharField(max_length=50)
    generalUserPassword=models.CharField(max_length=50)
    generalUserMail=models.CharField(max_length=50)
    generalUserDatabase=models.ManyToManyField(Mysqldbinfo)
    generalUserRole=models.CharField(max_length=13)
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.mysqldbalias,self.mysqldbname,self.mysqldbhost,self.mysqldbname,self.mysqldbport)
