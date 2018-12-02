from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,response
from django.shortcuts import render
from products.models import Product

def products_list(request,nazwa,opis,cena,status):
    Product.objects.create(nazwa=nazwa, opis=opis,cena=cena, status=status)

    return HttpResponse(nazwa,opis,cena, status)

def prodcuts_wypisz(request):
    objects = Product.objects.all()

    out=""
    for o in objects:
        out+=f"{o.nazwa}:{o.opis} {o.cena} {o.status}<br>"

    return render(
        request=request,
        template_name="products_list.html",
        context={"products": objects}
    )
