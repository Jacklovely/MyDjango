'''
Code description:
Create time: 2020/12/2
Developer: 李万洋
'''
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.results,name='vote'),
    url(r'^register/',views.register),
    url(r'^login/',views.login),
]