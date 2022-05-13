from django.shortcuts import render
from django.http import HttpResponse
from .models import ArmyShop, Course


def insert(request): 
    Course(name='데이터분석').save()
    Course(name='데이터수집').save()
    Course(name='웹개발').save()
    Course(name='인공지능').save()

    
    return HttpResponse('데이터 입력 완료')

def show(request):
    course = Course.objects.all()
   # result = ''
    #for c in course:
     #  result += c.name + '<br>'
    #return HttpResponse(result)
    return render(
        request, 'secondapp/show.html', 
        {'data': course}
    )

def army_shop(request):
   # shops=ArmyShop.objects.all()
    #print(shops)
    prd = request.GET.get('prd')
    if not prd : 
        prd = ' '
    shops=ArmyShop.objects.filter(name__contains=prd)
      
    return render(
        request, 'secondapp/army_shop.html',
        {'data':shops}
    )
    
def army_shop2(request,year,month):
    shops= ArmyShop.objects.filter(
        year=year,month=month
    )
    print(shops)
    return render(
        request, 'secondapp/army_shop.html',
        {'data':shops}
    )
    