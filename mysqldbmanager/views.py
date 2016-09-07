# coding=utf-8
from django.shortcuts import render_to_response,RequestContext
from mysqldbmanager.models import Mysqldbinfo
from mysqldbmanager.forms import inputdbsqlForm
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
import MySQLdb

# Create your views here.

def  inputsqlchoosedbinfo(request):
    if request.method == 'POST':
        form = inputdbsqlForm(request.POST)
        if form.is_valid():
            sqltext=form.cleaned_data['form_sqltext']
            mysqldbinfo=form.cleaned_data['form_mysqldbinfo']
            review_execute=form.cleaned_data['form_review_execute']
            request.session['mysqldbinfo']=mysqldbinfo
            request.session['sqltext']=sqltext
            request.session['review_execute']=review_execute
            return HttpResponseRedirect('/dealwithdbsqltext')

#            return render_to_response('showgetteddbsql.html',{'sqltext':sqltext,'mysqldbinfo':mysqldbinfo},context_instance=RequestContext(request))
#            return HttpResponseRedirect('/dealwith',{''})
        else:
            return render_to_response('inputdbandsql.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = inputdbsqlForm()
        return render_to_response('inputdbandsql.html', {'form': form}, context_instance=RequestContext(request))


def  dealwithdbsqltext(request):
    dealmysqldbinfo = request.session['mysqldbinfo']
    dealsqltext=request.session['sqltext']
    review_execute=request.session['review_execute']
    mysqldbalias = dealmysqldbinfo.mysqldbalias
    mysqldbname = dealmysqldbinfo.mysqldbname
    mysqldbuser = dealmysqldbinfo.mysqldbuser
    mysqldbpasswd = dealmysqldbinfo.mysqldbpasswd
    mysqldbhost = dealmysqldbinfo.mysqldbhost
    mysqldbport = dealmysqldbinfo.mysqldbport
    if review_execute=='1':
        revieworexecute = 'execute'
    else:
        revieworexecute = 'check'
    sql1 = '/*--user='+mysqldbuser+';--password='+mysqldbpasswd+';--host='+mysqldbhost+';--'+revieworexecute+'=1;--port='+mysqldbport+';*/\
        inception_magic_start;\
        use '+mysqldbname+';'
    sql2 = 'inception_magic_commit;'
    sql=sql1 + dealsqltext + sql2
    try:
        conn = MySQLdb.connect(host='10.150.21.120', user='wwn', passwd='123456', db='wwn', port=2222, use_unicode=True,charset="utf8")
#        conn=MySQLdb.connect(host='10.150.21.120',user='root',passwd='root',db='',port=2222,use_unicode=True, charset="utf8")
        cur=conn.cursor()
        ret=cur.execute(sql)
        result=cur.fetchall()
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        print field_names
        for row in result:
            print row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10]
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    review_result=result[1][4].split("\n")
    if review_result==[u'None']:
        if  review_execute=='1':
            review_result ='execute sucessful.'
        else:
            review_result='review is passed,no problem.'
    return render_to_response('revieworexecutesql.html', {'sql':sql,'review_result':review_result}, context_instance=RequestContext(request))

