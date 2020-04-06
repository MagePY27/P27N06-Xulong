from django.urls import path, re_path
from . import views, views1    #使用主路由+路由时需要导入文件
app_name = 'hello'

urlpatterns = [
    path('', views.index, name='hello'),
    path('list/',views.list, name='list'),
    path('list2/', views.list2, name='list2'),
    path('userlist/', views1.userlist, name='userlist'),
    path('useradd/', views1.useradd, name='useradd'),
    # path('usermodify/(?P<pk>[0-9]+)?/', views1.usermodify, name='usermodify'),
    re_path('usermodify/([0-9]{1,4})', views1.usermodify, name='usermodify'),
    re_path('userdel/([0-9]{1,4})', views1.userdel, name='userdel'),
]