from django.shortcuts import render
from myapp.models import Gogek
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


# Create your views here.
def Main(request):
    datas1 = Gogek.objects.all()
    return render(request, 'main.html', {'gogek':datas1})

def GogekCk(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    else:
        gogekname = request.POST.get('gogekname')
        gogektel = request.POST.get('gogektel')
    try:
        sql = "select gogek_damsano from Gogek where gogek_name = '{}' and gogek_tel = '{}'".format(gogekname, gogektel)
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor();
        cursor.execute(sql)
        data = cursor.fetchone()
        
        jnum = list(data)
        sql = "select jikwon_name, jikwon_jik, buser_name, buser_tel from jikwon, buser where buser_no = buser_num and jikwon_no='{}'".format(*jnum)
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor();
        cursor.execute(sql)
        data = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print('err : ', e)
        
    return render(request, 'jikwon.html', {'jikwondata':data})