from django.urls import path
from location import views
import location
app_name = 'location'


urlpatterns = [
path('party_data/',views.party_data, name='party_data'),
path('template/',views.template,name='template'),
path('place/', views.place, name='place'),
# path('youngdo/', views.youngdo,name='youngdo'),
# path('geumjeong/', views.geumjeong,name='geumjeong'),
# path('buk/', views.buk,name='buk'),
# path('busanjin/', views.busanjin,name='busanjin'),
# path('jung/', views.jung,name='jung'),
# path('haeundae/', views.haeundae,name='haeundae'),
# path('dong/', views.dong,name='dong'),
# path('dongnae/', views.dongnae,name='dongnae'),
# path('saha/', views.saha,name='saha'),
# path('gijang/', views.gijang,name='gijang'),
# path('sasang/', views.sasang,name='sasang'),
# path('gangseo/', views.gangseo,name='gangseo'),
]