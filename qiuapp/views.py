from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from qiuapp.models import PersonInfo
from qiuapp.models import User


def hello(request):
    return HttpResponse("你好")
    # result = {
    #     "code":0,
    #     "msg":"success!",
    #     "data":[{'hello':'word'}]
    # }
    # return JsonResponse(result)

def personView(request):
    info ={
        "nicheng":"",
        "name":"秋秋+",
        "age":20,
        "fancy":["python","pytest",'unittest'],
        "blog":{
            "url":"https://www.cnblogs.com/MrqiuS/",
            "img":"https://pic.cnblogs.com/avatar/1879595/20191125144908.png"
        },
        "a":'<a id ="lianjie" name="lianjie" href="https://www.cnblogs.com/MrqiuS/" target="_blank">点击'
    }
    class Blog():
        def __init__(self):
            self.name = "秋秋"
            self.age = "20"

        def guanzhu(self):
            return "1000"
        def fensi(self):
            return "1000"
    myblog = Blog()
    info["myblog"] = myblog

    return render(request,'personinfo.html',context=info)

def htmlview(request):
    context = {
        "title":"页面自定义名称"
    }
    return render(request,'artical_1.html',context=context)
def htmlview_2(request):

    return render(request,'artical_2.html')

def navlist(request):
    name_list= [
        {
            "type" :"科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算机/网络",
            "value": ["Java", "Python", "C语言"]
        }
    ]
    context = {"name_list":name_list}
    return render(request,'navlist.html',context=context)

def register(request):
    '''注册页面'''
    res = ''
    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('password')
        mail = request.POST.get('mail')
        #先查询数据库是否有此人
        user_list = User.objects.filter(user_name=username)
        if user_list:
            #如果已经注册提示已注册
            res = "%s用户已注册" % username
            return render(request,'register.html',{'rename':res})
        else:
            #如果没有注册，数据库插入一条数据
            user = User()
            user.user_name = username
            user.psw =psw
            user.mail = mail
            user.save()
            return render(request,'login.html',{'rename':res})
    return render(request,'register.html')

def login(request):
    #登录页面
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        #先查询数据库是否有此用户
        username = request.POST.get('username')
        password = request.POST.get('password')
        #查询用户名与密码
        user_obj = User.objects.filter(user_name=username,psw=password).first()
        if user_obj:
            return render(request,'gettel.html')
        else:
            return HttpResponse('用户名或密码错误')

def archive(request,year,month):
    res = {
        "code":0,
        "msg":"sucess",
        "data":[{
            "year":year,
            "month":month
        }]
    }
    return JsonResponse(res)

def get_tel(request):
    #获取提交的数据
    if request.method == "GET":
        telnum = request.GET.get('tel',1)#如果没获取到，默认1
        print('页面输入的手机号%s'%telnum)
        #根据手机号数据库查询
        #infos = PersonInfo.objects.filter(tel=telnum)
        # if infos:
        #     return render(request,'gettel.html',context=infos)
        # else:
        #     return render(request, 'gettel.html', context={ })

        try:
            info = PersonInfo.objects.get(tel=telnum)
        except :
            #raise Http404('Question does not exist')
            print('未查询到结果')
            info=None
        print('查询结果：%s'%info)
        a = {"info":info}
        return render(request,'gettel.html',context=a)
#
# def index(request):
#     return HttpResponse("这里是的投票站点")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s."%question_id)
