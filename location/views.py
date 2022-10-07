from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from .models import Party
from django.shortcuts import render

def template(request):
    return render(request, 'location/template.html')

def party_data(request):
    party = Party.objects.all()
    data= ''
    for p in party:
        data += p.title + '<br>'
        data += p.gu + '<br>'
        data += p.subtitle + '<br>'
        data += p.place + '<br>'
        data += p.address + '<br>'
        data += p.tel + '<br>'
        data += p.url + '<br>'
        data += p.info + '<br>'
        data += p.day + '<br>'
        data += p.des + '<br>'
        data += p.mid + '<br>'
        data += p.img + '<br>'
    return HttpResponse(data)

def place(request):
  gu = request.GET.get('gu')
  if not gu:
    gu = ''
  party_list = Party.objects.filter(gu__contains=gu)

  return render(request, 'location/festival.html', { 'party_list': party_list })
  
