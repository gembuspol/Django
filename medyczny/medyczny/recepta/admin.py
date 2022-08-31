from statistics import mode
from django.contrib import admin
from .models import adres,osoba,recepta,przepisane_leki
# Register your models here.

admin.site.register([adres,recepta,przepisane_leki])

class ReceptaInline(admin.TabularInline):
    model=recepta
    fk_name='pacjent'
    
@admin.register(osoba)
class osobaAdmin(admin.ModelAdmin):
    list_display=('imie','nazwisko','pesel','adres')
    inlines=[ReceptaInline]