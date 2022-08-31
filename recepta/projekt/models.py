import random
from django.db import models

# Create your models here.
class Adres(models.Model):
    miasto=models.CharField(max_length=40)
    kodPocztowy=models.CharField(max_length=6)
    ulica=models.CharField(max_length=150)
    nr_dom=models.CharField(max_length=10)
    nr_mieszkania=models.CharField(max_length=10)
    class Meta:
        verbose_name="Adres"
        verbose_name_plural="Adresy"
class Osoba(models.Model):
    idPacjent=models.IntegerField()
    imie=models.CharField(max_length=40)
    nazwisko=models.CharField(max_length=60)
    pesel=models.CharField(max_length=11)
    is_staff=models.BooleanField(default=False)
    specjalizacja=models.CharField(max_length=100, default=1)
    adres=models.ForeignKey(Adres,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return f'{self.idPacjent}-{self.imie} {self.nazwisko}'
    class Meta:
        verbose_name="Osoba"
        verbose_name_plural="Osoby"
def random_string():
    return str(random.randint(1000, 9999))

class Recepta(models.Model):
    kodRecepty=random_string()
    idPacjent=models.ForeignKey(Osoba,related_name='pacjent',on_delete=models.CASCADE)
    wystawca=models.ForeignKey(Osoba,on_delete=models.CASCADE)
    dataWystawienia=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Recepta"
        verbose_name_plural="Recepty"
    
    def __str__(self):
        return f'{self.kodRecepty} - {self.idPacjent} - {self.wystawca} - {self.dataWystawienia} - {self.przepisaneLeki}'
#lista=(n for n in range(1,101))
class Przepisane_leki(models.Model):
    recepta=models.ForeignKey(Recepta, on_delete=models.CASCADE)
    nazwa_leku=models.CharField(max_length=250)
    dawkowanie=models.CharField(max_length=2000)
    odplatnosc=models.IntegerField()
    class Meta:
        verbose_name="Przepisane Leki"
        verbose_name_plural="Przepisane Leki"
