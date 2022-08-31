import django

from django.urls import path
from . import views
app_name="projekt"

urlpatterns=[
    path('',views.index,name='index'),
    path('osoba/',views.osoba,name='osoba')
    
]