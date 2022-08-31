from django.contrib import admin

from projekt.models import Adres, Osoba, Przepisane_leki, Recepta

# Register your models here.
admin.site.register([Osoba,Recepta,Przepisane_leki,Adres])