#coding=utf8
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
from monitor.command.getoraclecommandresult import *

def index(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('index.html',dic)

def oracle_command(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('oracle_command.html',dic)


def commandresult(request):
    ipaddress  = str(request.GET['ipaddress']).split('-')[0]
    tnsname=str(request.GET['ipaddress']).split('-')[1]
    command_content  = str(request.GET['operate'])
    result=oraclelist.objects.all().order_by('tnsname')
    for i in result:
        if i.ipaddress==ipaddress:
            username =i.username
            password=i.password
            port=i.port
            break
    if command_content=='check_datafile_time':
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
            return HttpResponse(content)
        else:
            cursor = db.cursor()
            row=getdatafilecreationtime(cursor)
            cursor.close()
            db.close()
            title='数据文件创建时间-'+ipaddress+'-'+tnsname
            tr=['数据文件名称','文件大小','表空间','自动扩展','创建时间']
            dic ={'title':title,'tr':tr,'row':row}
            #return render_to_response('oracle_command_result1.html',dic)
            html= render_to_string('oracle_command_result_5.html',dic)
            return HttpResponse(html)

    elif command_content=='check_analyzed_time':
        table_name1=[]
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
            return HttpResponse(content)
        else:
            table_name  = str(request.GET['sql'])
            table_name=table_name.split()
            for i in table_name:
                table_name1.append('\''+str(i).strip().upper()+'\'')
            table_name=','.join(table_name1)
            cursor = db.cursor()
            row=getanalyzedtime(cursor,table_name)
            cursor.close()
            db.close()
            title='表分析的时间-'+ipaddress+'-'+tnsname
            tr=['OWNER','TABLE_NAME','NUM_ROWS','SAMPLE_SIZE','LAST_ANALYZED']
            dic ={'title':title,'tr':tr,'row':row}
            return render_to_response('oracle_command_result_5.html',dic)
    elif command_content=='check_segments_size':
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
            return HttpResponse(content)
        else:

            cursor = db.cursor()
            row=getsegmentssize(cursor)
            cursor.close()
            db.close()
            title='数据库段的大小-'+ipaddress+'-'+tnsname
            tr=['OWNER','SEGMENTS_NAME','SEGMENTS_TYPE','TABLESPACE_NAME','BYTES/GB']
            dic ={'title':title,'tr':tr,'row':row}
            return render_to_response('oracle_command_result_5.html',dic)

    elif command_content=='check_process_text':
        pid1=[]
        try:
            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
            return HttpResponse(content)
        else:
            pid  = str(request.GET['sql'])
            pid=pid.split()
            for i in pid:
                pid1.append('\''+str(i).strip().upper()+'\'')
            pid=','.join(pid1)
            cursor = db.cursor()
            row=getprocesstext(cursor,pid)
            cursor.close()
            db.close()
            title='数据库进程对用的SQL语句-'+ipaddress+'-'+tnsname
            tr=['SPID','SID','HASH_VALUE','SQL_TEXT','LOGON_TIME','PROGRAM']
            dic ={'title':title,'tr':tr,'row':row}
            return render_to_response('oracle_command_result_6.html',dic)
