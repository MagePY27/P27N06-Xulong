from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<p/> Hello Word,Hello, Django</p>")

# def index(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year')
#     month = kwargs.get('month')
#     return HttpResponse("year is %s, month is %s" % (year, month))


def index(request, **kwargs):
    print(request.scheme)
    print(request.method)
    print(request.headers)
    print(request.path)
    # print('Meta', request.META)
    print(request.GET)
    year = request.GET.get('year')
    month = request.GET.get('month')
    # return HttpResponse("<p/> Hello Word,Hello, Django</p>")
    return HttpResponse("year is %s, month is %s" % (year, month))

# def index(request):
#     user = "idc"
#     return render(request, "hello.html",{"user": user})


