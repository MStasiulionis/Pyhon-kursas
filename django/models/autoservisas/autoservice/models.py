import uuid
from django.db import models
from django.urls import reverse


class AutoModels(models.Model):
    brand_name = models.CharField('Pavadinimas', max_length=200)
    car_model = models.CharField('Modelis', max_length=200)

    def __str__(self):
        return f'{self.brand_name} {self.car_model}'

    class Meta:
        verbose_name = 'Modelis'
        verbose_name_plural = 'Modeliai'


class Car(models.Model):
    car_plate = models.CharField('Valstybinis numeris', max_length=200)
    car_model_id = models.ForeignKey('AutoModels', on_delete=models.SET_NULL, null=True)
    vin_code = models.CharField('VIN kodas', max_length=200)
    client = models.CharField('Kliento vardas', max_length=200)

    def __str__(self):
        return f'{self.car_model_id}'

    class Meta:
        verbose_name = 'Mašina'
        verbose_name_plural = 'Mašinos'


class Order(models.Model):
    date = models.DateField('Bus sutaisyta', null=True, blank=True)
    car_id = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    price = models.CharField("Kaina", max_length=200)

    def __str__(self):
        return f'{self.car_id}, {self.price}'


class OderLine(models.Model):
    service = models.ForeignKey('Services', on_delete=models.SET_NULL, null=True)
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    amount = models.CharField("Kiekis", max_length=200)
    price = models.IntegerField("Kaina")

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('t', 'Taisoma'),
        ('b', 'Baigta taisyti'),
        ('g', 'Galima pasiimti'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    def __str__(self):
        return f'{self.service}, {self.price}'


class Services(models.Model):
    name = models.CharField("Paslauga", max_length=200)
    price = models.IntegerField('Kaina')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

