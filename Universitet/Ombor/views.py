from django.shortcuts import render, redirect

from .models import *

def fanlar(request):
    if request.method=="POST":
        Fan.objects.create(
            nom=request.POST.get("fan"),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish"))
        )
        return  redirect("/fanlar/")


    n=Fan.objects.all()
    fan=request.GET.get("fan_nomi")
    if fan is not None:
        n=Fan.objects.filter(nom__contains=fan)
    data={
        "yonalishlar": Yonalish.objects.all(),
        "fanlar": n
    }
    return render(request, "Fanlar.html", data)


def ustozlar(request):

#Ustozlar jadvaliga malumot qo'shish qismi

    if request.method=="POST":
        Ustoz.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            yosh=request.POST.get("yosh"),
            daraja=request.POST.get("daraja"),
            fan=Fan.objects.get(id=request.POST.get("fan")),
        )
        return redirect("/ustozlar/")

#Ustozlar jadvalidan qidirish qismi

    n=Ustoz.objects.all()
    ustoz=request.GET.get("ustoz_ismi")
    if ustoz is not None:
        n=Ustoz.objects.filter(ism__contains=ustoz)
    data={
        "fanlar": Fan.objects.all(),
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

    if request.method=="POST":
        Yonalish.objects.create(
            nom=request.POST.get("yonalish"),
        )
        return redirect("/yonalish/")
    data={
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "Yonalishlar.html", data)

def y_ochir(req, pk):
    Yonalish.objects.get(id=pk).delete()
    return redirect("/yonalish/")









