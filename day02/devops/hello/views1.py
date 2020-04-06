from django.shortcuts import render, HttpResponse, get_object_or_404, Http404
from .models import Users
import traceback

def userlist(request):
    us = Users.objects.all()
    print(us)
    print(type(us))
    return render(request, 'userlist.html', {'us': us})
def useradd(request):
    msg = {}
    if request.method == "POST":
        try:
            # print('if',request.method)
            # name = request.POST.get('name','')
            # password = request.POST.get('password','')
            # sex = request.POST.get('sex')
            # print(name,password,sex)
            data = request.POST.dict()
            print(data)
            Users.objects.create(**data)
            msg = {'code':0, "result":"添加用户成功"}
        except Exception as e:
            print(e)
            msg = {'code':1, 'result':'添加用户失败'}
    return render(request, 'useradd.html', {'msg':msg})

def usermodify(request, id):
    print(request, id)
    # return HttpResponse('modify')
    msg = {}
    # print('kwargs', kwargs)
    # name = kwargs.get('id')
    name = Users.objects.get(id=id)
    user = get_object_or_404(Users, name=name)
    print("==" * 30)
    print(name, user)
    print('1',msg)
    if request.method == 'POST':
        try:
            data = request.POST.dict()
            print(data)
            Users.objects.filter(name=name).update(**data)
            msg = {'code':0, "result":"更新用户{}成功".format(data['name'])}
            print('try',msg)
        except Exception as e:
            print(e)
            msg = {'code':1, "result":"更新用户失败"}
            print('except', msg)
    else:
        print('else')
    return render(request, 'usermodify.html', {'user':user, 'msg':msg})

def userdel(request, id):
    msg = {}
    try:
        user = Users.objects.get(id=id)
    except Exception as e:
        print(e)
        raise Http404

    if request.method == 'POST':
        try:
            user = Users.objects.get(id=id)
            print(user)
            user.delete()
            msg = {'code':0, "result":"已删除用户{}".format(user)}
            print('try',msg)
        except Exception as e:
            print(e)
            msg = {'code':1, "result":"删除用户失败: %s" % traceback.format_exc()}
            print('except', msg)
    else:
        print('else')
    return render(request, 'userdel.html',{"user":user, 'msg':msg})