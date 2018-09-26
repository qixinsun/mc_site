from django.contrib import admin
from .models import *
from .utils import *
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'car_price', 'car_body_work', 'car_l_w_h',
                    'car_engine', 'car_gear_box', 'car_drive_way',
                    'car_fuel_type', 'car_oil_cons', 'car_color',
                    'car_href_pic', 'car_ld_pic', 'car_is_active',
                    'car_type', 'car_brand', 'car_spec_area']


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'type_desc']


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['barnd_name', 'barnd_desc']


class CarSpecialAreaAdmin(admin.ModelAdmin):
    list_display = ['spec_area_name', 'spec_area_desc']


class CarImageAdmin(admin.ModelAdmin):
    list_display = ['car_img', 'car']


class CarResevationListAdmin(admin.ModelAdmin):
    list_display = ['resevation_list_name','a_user_name', 'a_user_telephone',
                    'sale_name', 'sale_telephone', 'meet_place', 'meet_time','resevation_time']


class CarFavoriteAdmin(admin.ModelAdmin):
    list_display = ['favorite_user']


admin.site.register(Car, CarAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarSpecialArea, CarSpecialAreaAdmin)
admin.site.register(CarImage, CarImageAdmin)
admin.site.register(ResevationList, CarResevationListAdmin)
admin.site.register(Favorite, CarFavoriteAdmin)

class ImportDataAdmin(admin.ModelAdmin):
    list_display = ['file']
    list_filter = ['file', ]

    def save_model(self, request, obj, form, change):
        re = super().save_model(request, obj, form, change)
        import_data(self, request, obj, change)
        return re


class ImportDataFroAdmin(admin.ModelAdmin):
    list_display = ['file']
    list_filter = ['file', ]

    def save_model(self, request, obj, form, change):
        re = super().save_model(request, obj, form, change)
        import_data_fro(self, request, obj, change)
        return re

class ImportDataImagesAdmin(admin.ModelAdmin):
    list_display = ['file']
    list_filter = ['file', ]

    def save_model(self, request, obj, form, change):
        re = super().save_model(request, obj, form, change)
        import_images(self, request, obj, change)
        return re


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['intro1', 'pic', 'is_use']
    list_editable = ('is_use',)

class CarPriceAdmin(admin.ModelAdmin):
    list_display = ['car','shoufu','yuegong','qishu','weikuan']
    list_editable = ['shoufu','yuegong','qishu','weikuan']

admin.site.register(ImportData, ImportDataAdmin)
admin.site.register(ImportDataFro, ImportDataFroAdmin)
admin.site.register(ImportDataImages, ImportDataImagesAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(CarPrice, CarPriceAdmin)
