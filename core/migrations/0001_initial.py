# Generated by Django 4.2.4 on 2023-09-01 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=200)),
                ('nome_empresa', models.CharField(max_length=200)),
                ('categoria_empresa', models.CharField(max_length=200)),
                ('quitado', models.BooleanField()),
                ('stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stand')),
            ],
        ),
    ]
