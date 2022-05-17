from .models import Course
from django.http import HttpResponse
from django.urls import path
from . import views

app_name = 'secondapp'

urlpatterns = [
    # path('main/', views.main),
     path('insert/', views.insert),
     path('show/', views.show,name='show'),
     path('army_shop/', views.army_shop, name='army_shop'),
     path('army_shop/<int:year>/<int:month>', views.army_shop2)

]
