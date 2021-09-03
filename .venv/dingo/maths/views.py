# maths/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def maths(request):
    return HttpResponse("Tu będzie matma")

def add(request, a, b):
    a, b = int(a), int(b)
    wynik = a + b
    t = loader.get_template("maths/main.html")
#    print(type(c))
    return render(request, "maths/main.html", context = {"a": a, "b": b, "operacja": "+", "wynik": wynik})

def sub(request, a , b):
    return HttpResponse(a - b)
def mul(request, a, b):
    return HttpResponse(a * b)
def div(request, a, b):
    if b == 0:
        return HttpResponse("Pamietaj cholero nigdy nie dziel przez 0!!!")
    return HttpResponse (a / b)