from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<p>hello Word, Hello, Django!</p>")
    return render(request, 'index1.html', {'user':'hello Django'})

def list(request):
    # return HttpResponse('lisfffft')
    # books = ['python', 'java', 'Django']
    users = [
        # {'username':'k1', 'name_cn':'k1', 'age':18},
        # {'username': 'kf1', 'name_cn': 'kf1', 'age': 128},
    ]
    return render(request, 'hello/list.html', {'users':users})