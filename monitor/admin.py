from django.contrib import admin

# Register your models here.

from monitor.models import oraclelist
from monitor.models import oraclestatus


admin.site.register(oraclelist)
admin.site.register(oraclestatus)
