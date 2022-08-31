from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.template import loader
from .models import osoba, adres, recepta, przepisane_leki

# Create your views here.
def index(request):
    osoby=osoba.objects.all()
    adresy=adres.objects.all()
    context={'tytul':'Moja aplikacja do recept','lista_osob':osoby,'adres':adresy,}
    #return HttpResponse("To jest strona mojej aplikacji!!!")
    return render(request,'recepta/index.html',context)
def recepta1(request):
    dane=recepta.objects.all()
    return render(request,'recepta/recepta.html',{'tytul':'Podstrona do recept','lista_recept':dane})