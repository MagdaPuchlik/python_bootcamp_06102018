from django.db import models

# Create your models here.
class Product(models.Model):
    nazwa = models.CharField(max_length=16)
    opis = models.CharField(max_length=48)
    cena = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"Products:{self.nazwa}, opis prduktu: {self.opis}, cena{self.cena}, dostępny{self.status}"