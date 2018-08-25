from django.http import HttpResponse
from django.shortcuts import render
from movieApp.jsondata import Jsondata

# Create your views here.
from movieApp.models import Member


def rigist(request):
    return render(request,'register.html')


def toregist(request):

    name = request.POST.get('name')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    email = request.POST.get('email')
    img = request.POST.get('img')

    member = Member.objects.filter(name=name).first()
    print(member)
    if member:
        return HttpResponse('用户名已存在，请重新注册')

    if password == repassword:
        member1 = Member()
        member1.name = name
        member1.password = password
        member1.email = email
        member1.img = img
        member1.save()
        return HttpResponse('注册成功')
    else:
        return HttpResponse('前后密码不一致')


def login(request):
    return render(request,'login.html')


def home(request):
    Jdata = Jsondata.data
    lunbo =Jsondata.lunbo
    data={
        'Jdata':Jdata,
        'lunbo':lunbo
    }


    return render(request,'home.html',data)


def tologin(request):
    name = request.POST.get('name')
    password = request.POST.get('password')

    member = Member.objects.filter(name=name).first()

    if (member.name ==name) and (member.password ==password):
        request.session['name'] = name
        img = member.img
        return render(request,'home_logined.html',{'name':name,'img':img})
    else:
        return HttpResponse('用户名或密码错误')


def userinfo(request):
    name = request.session.get('name')
    return render(request,'userinfo_mod.html',{'name':name})


def changeUserInfo(request):

    email = request.POST.get('email')
    img = request.POST.get('img')
    name = request.session.get('name')


    member = Member.objects.filter(name=name).first()
    member.name = name
    member.email = email
    member.img = img
    member.save()
    return HttpResponse('个人信息修改成功')






