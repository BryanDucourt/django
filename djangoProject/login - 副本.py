from django.http import HttpResponse
from django.shortcuts import render
from testmodel.models import Test
import hashlib


def login(request):
    return render(request, 'login_form.html')


def register_post(request):
    return


def login_post(request):
    rst = {}
    if request.POST:
        if 'submit' in request.POST:
            name = request.POST['name']
            try:
                p = query(name)
            except Test.DoesNotExist:
                rst['clt'] = '用户不存在！'
            else:
                passwd = hashlib.md5()
                passwd.update(bytes(request.POST['pass'],encoding='utf-8'))
                if p.passwd != passwd.hexdigest():
                    rst['clt'] = '密码错误！'
        elif 'register' in request.POST:
            rst['clt'] = insert(request.POST['name'], request.POST['pass'])
    return render(request, 'login_form.html', rst)


def query(name):
    respose=""
    _list = Test.objects.all()
    respose = Test.objects.get(name=name)
    return respose


def insert(name, passwd):
    try:
        Test.objects.get(name=name)
    except Test.DoesNotExist:
        pwd = hashlib.md5()
        pwd.update(bytes(passwd,encoding='utf-8'))
        user = Test(name=name, passwd=pwd.hexdigest())
        user.save()
        return '注册成功'
    else:
        return '用户名已存在！'
