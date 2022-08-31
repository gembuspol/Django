from django.contrib import admin

# Register your models here.
from czat import models  # importujemy nasz model

# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(models.Wiadomosc)