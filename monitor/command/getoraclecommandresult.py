import re
import os
import subprocess
import cx_Oracle
def getdatafilecreationtime(cursor):
    fp=open('/home/oracle/mysite/monitor/command/oracle_command/getdatafilecreationtime.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

