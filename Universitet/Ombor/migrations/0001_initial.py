# Generated by Django 5.0.1 on 2024-01-15 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=20)),
                ('yosh', models.PositiveIntegerField()),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr')], max_length=20)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ombor.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ombor.yonalish'),
        ),
    ]
