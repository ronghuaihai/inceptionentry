# coding=utf-8
from django.forms import ModelForm
from django import forms
from mysqldbmanager.models import Mysqldbinfo

REVIEW_EXECUTE_CHOICES=(
('0',u'只审核不执行'),
('1',u'审核并执行')
)

class inputdbsqlForm(forms.Form):
         form_sqltext=forms.CharField(required=True,widget=forms.Textarea,label=u'请输入您要执行的sql文本：',error_messages={'required':u'必须输入要执行的sql'},)
         form_mysqldbinfo=forms.ModelChoiceField(queryset=Mysqldbinfo.objects.order_by('mysqldbalias'),required=True,label=u'请选择数据库：',error_messages={'required':u'必须选择一个数据库'},)
         form_review_execute=forms.ChoiceField(widget=forms.RadioSelect,choices=REVIEW_EXECUTE_CHOICES,label=u'请选择工作模式',required=True,error_messages={'required':u'必须选择一个工作模式'})

        # mysqldbmodel=Mysqldbinfo
        # fields=('sqltext',)
