from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<p>hello Word, Hello, Django!</p>")
    return render(request, 'index.html', {'user':'hello Django'})

def list(request):
    # return HttpResponse('lisfffft')
    classname = "Devops"
    books = ['python', 'java', 'Django']   #列表
    user = {'name':'tom', 'age':18}       #字典
    userlist = [
        {'username':'zhang3', 'name_cn':'张三', 'age':18},
        {'username': 'li4', 'name_cn': '李四', 'age': 20},
        {'username': 'wang5', 'name_cn': '王五', 'age': 25},
    ]
    return render(request, 'list.html', {'classname':classname,'books':books,
                                         'user':user, 'userlist':userlist})

def list2(request):
    users = [
        {'username':'zhang3', 'name_cn':'张三', 'age':18},
        {'username': 'li4', 'name_cn': '李四', 'age': 20},
        {'username': 'wang5', 'name_cn': '王五', 'age': 25},
    ]
    return render(request, 'list2.html', {'users':users})

from .models import Users
def userlist(request):
    us = Users.objects.all()
    print(us)
    print(type(us))
    return render(request, 'userlist.html', {'us': us})
