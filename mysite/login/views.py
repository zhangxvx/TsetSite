from django.http import HttpResponse
from django.shortcuts import render

from .models import User
# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def register(request):
    username = request.POST['username']
    userInfor=User.objects.get(name=username)
    userid=userInfor.id
    email=userInfor.email
    password=userInfor.password
    return render(request, 'login/welc.html', {'userid':userid,'username': username,'email':email,'password':password})
