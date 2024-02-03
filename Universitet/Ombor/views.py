from django.shortcuts import render, redirect

from .models import *


def fanlarni_tahrirlash(request, pk):
    if request.method == 'POST':
        fanlar = Fan.objects.get(id=pk)

        fanlar.nom = request.POST.get('nom')
        fanlar.yonalish=Yonalish.objects.get(id=request.POST.get('yonalish'))
        fanlar.save()

        return redirect('/fanlar/')

    data = {
        'fanlar': Fan.objects.get(id=pk),
        'yonalishlar': Yonalish.objects.all()
    }
    return render(request, 'Fanlarni_tahirilash.html', data)


def fanlar(request):
    if request.method == "POST":
        Fan.objects.create(
            nom=request.POST.get("fan"),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish"))
        )
        return redirect("/fanlar/")

    n = Fan.objects.all()
    fan = request.GET.get("fan_nomi")
    if fan is not None:
        n = Fan.objects.filter(nom__contains=fan)
    data = {
        "yonalishlar": Yonalish.objects.all(),
        "fanlar": n
    }
    return render(request, "Fanlar.html", data)



def Ustozni_tahrirlash(request, pk):
    if request.method=='POST':
        ustoz=Ustoz.objects.get(id=pk)
        ustoz.ism=request.POST.get('ism')
        ustoz.jins=request.POST.get('jins')
        ustoz.yosh=request.POST.get('yosh')
        ustoz.daraja=request.POST.get('daraja')
        ustoz.fan=Fan.objects.get(id=request.POST.get('fan'))
        ustoz.save()

        return redirect('/ustozlar/')

    contex={
        'ustozlar': Ustoz.objects.get(id=pk),
        'fanlar': Fan.objects.all()
    }

    return render(request, 'Ustozlarni_tahrirlash.html', contex)


def ustozlar(request):
    # Ustozlar jadvaliga malumot qo'shish qismi

    if request.method == "POST":
        Ustoz.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            yosh=request.POST.get("yosh"),
            daraja=request.POST.get("daraja"),
            fan=Fan.objects.get(id=request.POST.get("fan")),
        )
        return redirect("/ustozlar/")

    # Ustozlar jadvalidan qidirish qismi

    n = Ustoz.objects.all()
    ustoz = request.GET.get("ustoz_ismi")
    if ustoz is not None:
        n = Ustoz.objects.filter(ism__contains=ustoz)
    data = {
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


def yonalish_tahrirlash(request, pk):
    if request.method == "POST":
        yonalish = Yonalish.objects.get(id=pk)
        yonalish.nom = request.POST['nom']
        if request.POST.get('active', False) == "on":
            yonalish.active = True

        else:
            yonalish.active = False

        yonalish.save()

        return redirect('/yonalish/')

    data = {
        "yonalish": Yonalish.objects.get(id=pk)

    }
    return render(request, 'Yonalishni_tahrirlash.html', data)


def yonalish(request):
    if request.method == "POST":
        if request.POST.get("active") == 'on':
            natija = True
        else:
            natija = False
        Yonalish.objects.create(
            nom=request.POST.get("yonalish"),
            active=natija,
        )
        return redirect("/yonalish/")
    data = {
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "Yonalishlar.html", data)


def y_ochir(req, pk):
    Yonalish.objects.get(id=pk).delete()
    return redirect("/yonalish/")
