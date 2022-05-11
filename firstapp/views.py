from django.http import HttpResponse
from .models import Curriculum
from django.shortcuts import render

def show(request):
    curriculum = Curriculum.objects.all()
    #result = ''
    #for c in curriculum:
     #   result += c.name + '<br>'
    #return HttpResponse(result)
    return render(request, 'show.html',
     {'data':Curriculum})


def insert(request):   
# 1-linux 입력
    Curriculum.objects.create(name='linux')
# 2-python 입력
    c = Curriculum(name='python')
    c.save()
# 3-html/css/js 입력
    Curriculum(name='python').save()
# 4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')
