from django.http import Http404,HttpResponse
from django.template.loader import get_template
import datetime
from django.template import Context
from django.shortcuts import render_to_response,RequestContext
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from mysqldbmanager.forms import inputdbsqlForm
from django.http import HttpResponseRedirect


#@csrf_protect
def hello(request):
    if request.method=='POST':
        form = inputdbsqlForm(request.POST)
        if form.is_valid():
#            sqltext = form.cleaned_data['form_sqltext']
            return HttpResponseRedirect('/')
    else:
        form=inputdbsqlForm()
    return render_to_response('hello.html' ,{'form':form},context_instance=RequestContext(request))


def testhtml(request):
    return render_to_response('test1.html',context_instance=RequestContext(request))

def current_datetime(request):
    now=datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
#    t=get_template('current_datetime.html')
#    html=t.render(Context({'current_date':now}))
#    return HttpResponse(html)

def userlogin(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def userregister(request):
    return render_to_response('userregister.html',context_instance=RequestContext(request))



