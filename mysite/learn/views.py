# coding:utf-8
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Grade


def index(request):
    # return HttpResponse(u"Welcome!")
    string = "欢迎来到Django!"
    tutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    inforDict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    list = map(str,range(100))
    return render(request, 'learn/index.html', {"string": string,"tutorialList":tutorialList,
        "inforDict":inforDict,"list":list})
 

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('learn:add2', args=(a, b))
    )


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
 
def getGrades(request):
    # 获取所有班级
    grades = Grade.objects.all()
    context = {'gradess':grades}
    return render(request,'learn/Grade.html',context)
