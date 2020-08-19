from django.http import HttpResponse
from django.shortcuts import render
from login.models import Login
import hashlib


def query(name):
    _list = Login.objects.all()
    response = Login.objects.get(name=name)
    return response


def login(request):
    name = request.POST['name']
    try:
        p = query(name)
    except Login.DoesNotExist:
        rst = '用户不存在！'
        return rst
    else:
        passwd = hashlib.md5()
        passwd.update(bytes(request.POST['pass'], encoding='utf-8'))
        if p.passwd != passwd.hexdigest():
            rst = '密码错误！'
            return rst
        else:
            return '1'


def register(request):
    rst = insert(request.POST['name'], request.POST['pass'])
    return rst


def insert(name, passwd):
    try:
        Login.objects.get(name=name)
    except Login.DoesNotExist:
        pwd = hashlib.md5()
        pwd.update(bytes(passwd, encoding='utf-8'))
        user = Login(name=name, passwd=pwd.hexdigest())
        user.save()
        return '注册成功'
    else:
        return '用户名已存在！'
