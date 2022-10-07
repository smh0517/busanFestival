from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse  # JSON 응답
from map.models import PartyMap
from django.forms.models import model_to_dict


def index(request):
  # m = hashlib.sha256()
  # m.update(b"testtest")
  # print( m.hexdigest() )
  # s = '37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578'
  # print( len(s) )
  return render(request, 'index.html')


# map 페이지

def map(request):
  return render(request, 'map.html')


def map_data(request):
  lat = request.GET.get('lat')
  lng = request.GET.get('lng')

  data = PartyMap.objects.raw('''
    SELECT *,
       (6371 * acos(
         cos(radians(%s))
         * cos(radians(lat))
         * cos(radians(lng) - radians(%s))
         + sin(radians(%s))
         * sin(radians(lat)))) AS distance
     FROM party_map
    HAVING distance <= %s
    ORDER BY distance''' % (lat, lng, lat, 30))
  map_list = []
  for d in data:
    d = model_to_dict(d)  # QuerySet -> Dict
    map_list.append(d)
  # dict가 아닌 자료는 항상 safe=False 옵션 사용
  return JsonResponse(map_list, safe=False)


# contact 페이지

def contact(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    comment = request.POST.get('comment')
    #         발신자주소, 수신자주소, 메시지
    send_mail('algus4448@gmail.com', email, comment)
    return render(request, 'contact_success.html')

  return render(request, 'contact.html')

import smtplib
from email.mime.text import MIMEText
 
def send_mail(from_email, to_email, msg):
  # SMTP 설정
  smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  # 인증정보 설정
  smtp.login(from_email, 'kwlirxmirfhwzdre')
  msg = MIMEText(msg)
  # 제목
  msg['Subject'] = '[문의사항]' + to_email
  # 수신 이메일
  msg['To'] = from_email
  smtp.sendmail(from_email, from_email, msg.as_string())
  smtp.quit()


def search(request):
    title = request.GET.get('title')
    return HttpResponse('search : %s' % (title))

def info(request):
    id = request.GET.get('id')
    return HttpResponse('id : %s' % (id))
