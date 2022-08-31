from django.http import HttpResponse
from django.shortcuts import render

from projekt.models import Osoba

# Create your views here.
def index(request):
    return HttpResponse("To jest strona mojej aplikacji!!!")
def osoba(request):
    lista_osob=Osoba.objects.all()
    wyjscie='<p>'.join(['<p>'+l.imie+l.nazwisko for l in lista_osob])
    #return render(request,'projekt\osoba.html')
    return HttpResponse(f"To są osoby {wyjscie}")