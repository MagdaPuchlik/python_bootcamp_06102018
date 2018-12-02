from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Math(models.Model): #określamy dziedziczenie
    operation = models.CharField(max_length=10) #domyslnie pole jest wymagane, chyba że wpiszę np null = True
    arg_a = models.IntegerField()
    arg_b = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

#dajemy znać Django że zorbiliśmy powyższe ograniczenia czyli model i że chcemy żeby Django tez aktualizował te informacje

    def __str__(self):
        return f"Math operation:{self.operation},arguments: {self.arg_a},{self.arg_b}"