from django.shortcuts import render
import MySQLdb
import cx_Oracle
import time
import datetime
from django.views.decorators.http import require_http_methods
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpRequest
from django import template
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from monitor.models import *
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Group

def index(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('index.html',dic)

def oracle_command(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('oracle_command.html',dic)
