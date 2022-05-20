from django.urls import path
from . import views

urlpatterns = [
    path('img_list/', views.img_list, name='img_list'),
]
