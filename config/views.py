from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index1(request):
    return HttpResponse('<u>Hello</u>')


def index2(request):
    return HttpResponse('<u>Hi</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

def Home(request):
    return HttpResponse('Home')

def index(request):
    return render(request, 'index.html',{})