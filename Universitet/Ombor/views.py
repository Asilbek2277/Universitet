from django.shortcuts import render, redirect

from .models import *

def fanlar(request):
    n=Fan.objects.all()
    fan=request.GET.get("fan_nomi")
    if fan is not None:
        n=Fan.objects.filter(nom__contains=fan)
    data={
        "fanlar": n
    }
    return render(request, "Fanlar.html", data)


def ustozlar(request):
    n=Ustoz.objects.all()
    ustoz=request.GET.get("ustoz_ismi")
    if ustoz is not None:
        n=Ustoz.objects.filter(ism__contains=ustoz)
    data={
        "ustozlar": n
    }
    return render(request, "Ustozlar.html", data)


def ustozni_ochirish(req, pk):
    Ustoz.objects.get(id=pk).delete()
    return redirect("/ustozlar/")

def fanni_ochirish(req, pk):
    Fan.objects.get(id=pk).delete()
    return redirect("/fanlar/")


def yonalish(request):
    data={
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "Yonalishlar.html", data)

def y_ochir(req, pk):
    Yonalish.objects.get(id=pk).delete()
    return redirect("/yonalish/")









