import django

from django.urls import path
from . import views
app_name="ankieta"

urlpatterns=[
    path('',views.index,name='index'),
    path('pytania/',views.pytania,name='pytania'),
    path('pytania/<int:pytanie_id>/',views.szczegoly,name='szczegoly'),
    path('pytania/<int:pytanie_id>/glosuj/',views.glosuj,name='glosuj'),
    path('pytania/<int:pytanie_id>/wyniki/',views.pokaz_rezultat_glosowania,name='wyniki')
]