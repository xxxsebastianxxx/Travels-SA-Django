# Generated by Django 4.0.4 on 2022-05-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inicio', models.CharField(max_length=80)),
                ('destino', models.CharField(max_length=80)),
                ('tarifa', models.BigIntegerField(max_length=80)),
                ('horario', models.CharField(max_length=80)),
            ],
        ),
    ]
