from django.db import models

class Yonalish(models.Model):
    nom=models.CharField(max_length=20)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom=models.CharField(max_length=20)
    yonalish=models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Ustoz(models.Model):
    ism=models.CharField(max_length=20)
    jins=models.CharField(max_length=20, choices=[("Erkak", "Erkak"), ("Ayol", "Ayol")])
    yosh=models.PositiveIntegerField()
    daraja=models.CharField(max_length=20, choices=[("Bakalavr", "Bakalavr"), ("Magistr", "Magistr")])
    fan=models.ForeignKey(Fan, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.ism}"