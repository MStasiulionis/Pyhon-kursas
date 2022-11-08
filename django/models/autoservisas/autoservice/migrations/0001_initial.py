# Generated by Django 4.1.1 on 2022-10-13 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200, verbose_name='Pavadinimas')),
                ('car_model', models.CharField(max_length=200, verbose_name='Modelis')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_plate', models.CharField(max_length=200, verbose_name='Valstybinis numeris')),
                ('vin_code', models.CharField(max_length=200, verbose_name='VIN kodas')),
                ('client', models.CharField(max_length=200, verbose_name='Kliento vardas')),
                ('car_model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.automodels')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Paslauga')),
                ('price', models.IntegerField(max_length=10, verbose_name='Kaina')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, verbose_name='Data')),
                ('price', models.CharField(max_length=200, verbose_name='Kaina')),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.car')),
            ],
        ),
        migrations.CreateModel(
            name='OderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200, verbose_name='Kiekis')),
                ('price', models.CharField(max_length=200, verbose_name='Kaina')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.order')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.services')),
            ],
        ),
    ]
