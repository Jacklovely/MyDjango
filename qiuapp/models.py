import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    #是否在当前发布的问卷
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class PersonInfo(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    age = models.IntegerField(null=True)
    mail = models.EmailField(default="123@qq.com")#默认值
    tel = models.BigIntegerField(null=True,blank=True)
    datatime = models.DateTimeField(auto_now=True, null=True, blank=True)  # 020-06-30 11:22:01
    create_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True,null=True,blank=True)  # 更新时间

class PersonInfoNew(models.Model):
    uid = models.IntegerField(primary_key=True)#主键
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True)
    text = models.TextField(null=True, blank=True)
    img = models.ImageField(default='')
    file = models.FileField(default='')
    status = models.BooleanField(default=True)  # bool值
    data = models.DateField(auto_now=True,null=True,blank=True)  # 2020-06-30
    time = models.TimeField(auto_now=True,null=True,blank=True)  # 11:22:01
    datatime = models.DateTimeField(auto_now=True,null=True,blank=True)  # 020-06-30 11:22:01

class User(models.Model):
    user_name = models.CharField(max_length=30,primary_key=True)
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
