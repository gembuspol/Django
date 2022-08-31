from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .models import Pytanie, Glosy
from django.template import loader
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def index(request):
    return HttpResponse("To jest strona mojej aplikacji!!!")
def pytania(request):
    #return HttpResponse("To są wszystkie pytania")
    lista_ostatnich_pytan=Pytanie.objects.all()[:5]
    #wyjscie='</p>'.join(['<p>'+l.tekst_pytania for l in lista_ostatnich_pytan])
    #template = loader.get_template('ankieta\templates\ankieta\pytania.html')
    
    return render(request,'ankieta\pytania.html',{'lista_ostatnich_pytan':lista_ostatnich_pytan})

def szczegoly(request, pytanie_id):
    pytanie=get_object_or_404(Pytanie, pk=pytanie_id)
    #return HttpResponse(f"To są szczegóły pytania {pytanie_id}")
    return render(request, 'ankieta/szczegoly.html',{'pytanie':pytanie})

def wyniki(request,pytanie_id):
    return HttpResponse(f"To są wyniki pytania {pytanie_id}")

def glosuj(request, pytanie_id):
    print(request.POST['Wybor'])
    Glosy.objects.create(pytanie_id=pytanie_id,odpowiedz_id=request.POST['Wybor'], uzytkownik=get_client_ip(request))
    return HttpResponseRedirect(f"/ankieta/pytania/{pytanie_id}/wyniki")
def pokaz_rezultat_glosowania(request,pytanie_id):
    #get_object_or_404(Pytanie,pytanie_id)
    glosy=Glosy.objects.filter(pytanie_id=pytanie_id)
    odpowiedzi={}
    for glos in glosy:
        if current_value:=odpowiedzi.get(glos.odpowiedz.tekst_wyboru):
            odpowiedzi[glos.odpowiedz.tekst_wyboru]=current_value+1
        else:
            odpowiedzi[glos.odpowiedz.tekst_wyboru]=1
    return JsonResponse(odpowiedzi)