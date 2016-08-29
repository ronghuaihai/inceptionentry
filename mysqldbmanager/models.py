from __future__ import unicode_literals

from django.db import models




class Mysqldbinfo(models.Model):
    mysqldbalias=models.CharField(max_length=50)
    mysqldbname=models.CharField(max_length=50)
    mysqldbuser=models.CharField(max_length=50)
    mysqldbpasswd=models.CharField(max_length=50)
    mysqldbhost=models.CharField(max_length=50)
    mysqldbport=models.CharField(max_length=20)
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.mysqldbalias,self.mysqldbname,self.mysqldbhost,self.mysqldbname,self.mysqldbport)
#,self.mysqldbname,self.mysqldbuser,self.mysqldbpasswd,self.mysqldbhost,self.mysqldbport



