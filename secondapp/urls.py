from .models import Course
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    # path('main/', views.main),
     path('insert/', views.insert),
     path('show/', views.show)
    # path('insert/', views.insert),
    # path('show/', views.show)
]
def show(request):
    course = course.objects.all()
    result = ''
    for c in course:
        result += c.name + '<br>'
    return HttpResponse(result)