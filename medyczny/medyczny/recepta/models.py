from datetime import datetime
from random import randint
from statistics import mode
from tkinter import CASCADE
from django.db import models
def random_string():
    return str(randint(1000, 9999))
class adres(models.Model):
    miasto = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=6)
    ulica = models.CharField(max_length=250)
    nr_domu = models.CharField(max_length=5)
    nr_mieszkania = models.CharField(max_length=4)
    def __str__(self):
        return f'{self.miasto}, {self.ulica} {self.nr_domu}' 
    class Meta:
        verbose_name="Adres"
        verbose_name_plural="Adresy"
        ordering= ("miasto",)
class osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel= models.CharField(max_length=11)
    is_staff=models.BooleanField(default=False)
    specjalizacja=models.CharField(max_length=100)
    adres=models.ForeignKey(adres, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nazwisko}, {self.imie}' 
    class Meta:
        verbose_name="Osoba"
        verbose_name_plural="Osoby"
        ordering= ("nazwisko",)
class recepta(models.Model):
    kod_recepty=random_string()
    pacjent=models.ForeignKey(osoba, related_name='pacjent', on_delete=models.CASCADE)
    wystawca=models.ForeignKey(osoba, on_delete=models.CASCADE)
    data_wystawienia= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        #return f'{self.kod_recepty}, {self.__id__}' 
        return f'{self.kod_recepty}' 
    class Meta:
        verbose_name="Recepta"
        verbose_name_plural="Recepty"
        ordering= ("-data_wystawienia",)
    # payment_fraction = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
class przepisane_leki(models.Model):
    recepta=models.ForeignKey(recepta, on_delete=models.CASCADE)
    nazwa_leku=models.CharField(max_length=250)
    dawkowanie=models.CharField(max_length=2000)
    odplatnosc=models.IntegerField()
    def __str__(self):
        return f'{self.nazwa_leku.upper()}' 
    class Meta:
        verbose_name="Lek"
        verbose_name_plural="Leki"
        ordering= ("nazwa_leku",)