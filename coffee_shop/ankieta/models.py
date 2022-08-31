from datetime import datetime
from tabnanny import verbose
from django.db import models

# Create your models here.
class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=400)
    data_publikacji=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.tekst_pytania.upper()} - {self.data_publikacji.strftime("%m/%d/%Y, %H:%M:%S")}'
    class Meta:
        verbose_name="Pytanie"
        verbose_name_plural="Pytania"
        ordering=("data_publikacji",)

class Odpowiedz(models.Model):
    pytanie=models.ForeignKey(Pytanie,on_delete=models.CASCADE)
    tekst_wyboru=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.pytanie} - {self.tekst_wyboru}'
    class Meta:
        verbose_name="Odpowiedź"
        verbose_name_plural="Odpowiedzi"
   
class Glosy(models.Model):
    odpowiedz=models.ForeignKey(Odpowiedz,on_delete=models.CASCADE)
    pytanie=models.ForeignKey(Pytanie,on_delete=models.CASCADE)
    uzytkownik=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.uzytkownik} - {self.pytanie.id} - {self.odpowiedz.id}'
    class Meta:
        verbose_name="Głos"
        verbose_name_plural="Głosy"
