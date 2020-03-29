from django.urls import path, re_path

from . import views
urlpatterns = [
    path('', views.index, name='index')
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index')
]