from django.urls import path
from . import views    #使用主路由+路由时需要导入文件

urlpatterns = [
    path('', views.index, name='hello'),
    path('list/',views.list, name='list'),
    path('list2/', views.list2, name='list2'),

]