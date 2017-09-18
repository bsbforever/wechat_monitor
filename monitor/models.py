from __future__ import unicode_literals

from django.db import models

# Create your models here.


class oraclelist(models.Model):
    ipaddress=models.GenericIPAddressField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    port=models.CharField(max_length=50)
    tnsname=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    charset=models.CharField(max_length=100)
    ncharset=models.CharField(max_length=100)
    hostname=models.CharField(max_length=100)
    alertpath=models.CharField(max_length=300)
    content=models.CharField(max_length=300)
    monitor_type=models.IntegerField(default=1)
    performance_type=models.IntegerField(default=0)
    hit_type=models.IntegerField(default=1)
    def __unicode__(self):
        return self.tnsname
    class Meta:
        app_label='monitor'


class oraclestatus(models.Model):
    tnsname=models.CharField(max_length=100)
    ipaddress=models.GenericIPAddressField()
    dbsize=models.CharField(max_length=50)
    tbstatus=models.CharField(max_length=200)
    host_name=models.CharField(max_length=50,default='host')
    version=models.CharField(max_length=50,default='10')
    startup_time=models.CharField(max_length=50,default='2015')
    archiver=models.CharField(max_length=20,default='opened')
    sga_size=models.IntegerField(default=0)

    def __unicode__(self):
        return self.tnsname
    class Meta:
        app_label='monitor'
