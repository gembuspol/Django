from django.contrib import admin
from  .models import  Pytanie, Odpowiedz, Glosy
# Register your models here.

admin.site.register([Odpowiedz,Glosy])

class OdpowiedzInline(admin.TabularInline):
    model=Odpowiedz

@admin.register(Pytanie)
class PytanieAdmin(admin.ModelAdmin):
    list_display=('tekst_pytania','data_publikacji')
    inlines=[OdpowiedzInline]

    