from django.contrib import admin
from .models import AutoModels, Car, Order, OderLine, Services


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_plate', 'client', 'vin_code', 'car_model_id')
    search_fields = ('car_model_id__car_model', 'car_model_id__brand_name', 'client', 'vin_code')


class AutoModelsAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'car_model')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'car_id')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(AutoModels, AutoModelsAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OderLine)
admin.site.register(Services, ServicesAdmin)
