# Generated by Django 3.1.5 on 2021-03-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[('tel_fixe', models.CharField(max_length=20)),
                ('tel_mobile', models.CharField(max_length=20)),
                ('mot_de_passe', models.CharField(max_length=32)),
            ],
        ),
    ]
