"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path
#从hello app中定义一个哪view.py模块index函数来处理hello这个用户请求
# from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 如果访问hello, 总入口直接指向具体app的具体方法，一旦app过多，路由过多，主路口不堪重负，要分而治之
    # path('hello', views.index)
    #当访问具体app的时候，不指定具体方法，而是告诉你去具体app的usrls.py定义
    path('hello/', include('hello.urls'), name='hello'),
    # path('list', include('list.usrl'), name='list'),
]
