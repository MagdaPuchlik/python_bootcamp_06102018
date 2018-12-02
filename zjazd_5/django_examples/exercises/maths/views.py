from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,response
from django.shortcuts import render
from maths.models import Math

@login_required() # aby zobaczyć dane należy się zalogować


def math_operations(request, operation, arg_a, arg_b):

    if request.user:
        Math.objects.create(operation=operation,arg_a=arg_a,arg_b=arg_b, user = request.user)
    else:
        return HttpResponse(calculate(operation,arg_a,arg_b))

def calculate(operation,arg_a,arg_b):
    result = None
    if operation =='add':
        result = arg_a+arg_b
    elif operation =='sub':
        result = arg_a-arg_b
    return result


def math_list(request):
    objects = Math.objects.all()

    out=""
    for o in objects:
        out+=f"{o.operation}:{o.arg_a} {o.arg_b}<br>"

    return render(
        request=request,
        template_name="math_list.html",
        context={"maths": objects}
    )

def math_details(request,id):
    m=Math.objects.get(pk=id)# pobieramy obiekt primary key (pk) równe id

    return render(
        request=request,
        template_name="math_details.html",
        context={"math": m, "wynik":calculate(m.operation,m.arg_a,m.arg_b)}
    )

# def math_details(request,id):
#     m=Math.objects.get(pk=id)# pobieramy obiekt primary key (pk) równe id
#
#     out = f"""
#     Operacja:{m.operation}<br>
#     arg_1: {m.arg_a}<br>
#     arg_2: {m.arg_b}<br>
#     ------------------<br>
#     wynik: {calculate(m.operation,m.arg_a,m.arg_b)}
#     """
#     return HttpResponse(out)