from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.shortcuts import render

from thirdapp.forms import OwnerForm
from .models import Shop, JejuOlle, Owner , Hospital

def owner(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    
    owner = Owner(name=name)
    owner.save()

    return HttpResponse('주인 정보 등록 완료')
  return render(request, 'thirdapp/owner.html', {})

def shop(request):
    shop_list = Shop.objects.all()
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
)

def jeju_olle_ajax(request):
  return render(
    request,'thirdapp/jeju_olle_ajax.html', {}
  )

def jeju_olle(request):
    #jeju_olle_list = JejuOlle.objects.all()
   # print(jeju_olle_list)
    time = request.GET.get('time')
    if not time: time= ' '
    jeju_olle_list = JejuOlle.objects.filter(
        time_info__contains=time
    )
    return render(
        request,
        'thirdapp/jeju_olle.html',
        {'jeju_olle_list': jeju_olle_list}
)

def hospital(requset):
  hospitals = Hospital.objects.all()
  return render(
    requset, 'thirdapp/hospital.html',{'hospitals':hospitals}
  )

def form_model(request):
  if request.method == 'POST':
    form = OwnerForm(request.POST)
    if form.is_valid():
      owner = form.save(commit=False)
# (필요하다면) 데이터 추가 / 변경
      owner.save()
      return redirect('/third/form/model/')
  else:
      form = OwnerForm()
  return render(
      request, 'thirdapp/form_model.html',
    {'form': form}
)