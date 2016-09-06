from inceptionentry.views import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
import mysqldbmanager.views as mysqldbviews



urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^currenttime/$',current_datetime),
    url(r'^inputdbsql/$',mysqldbviews.inputsqlchoosedbinfo),
    url(r'^dealwithdbsqltext/$',mysqldbviews.dealwithdbsqltext),
    url(r'^testhtml/$',testhtml),
    url(r'^login/$',userlogin),
    url(r'^userregister/$',userregister),
]
