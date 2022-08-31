import django

from django.urls import path
from . import views
app_name="recepta"

urlpatterns=[
    path('',views.index,name='index'),
    path('recepta1/',views.recepta1,name='recepta1'),
    
]