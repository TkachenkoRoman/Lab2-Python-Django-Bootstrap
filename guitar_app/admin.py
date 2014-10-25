from django.contrib import admin
from guitar_app import models

# Register your models here.

class ProduserAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    list_filter = ['rating']

class BodyAdmin(admin.ModelAdmin):
    list_display = ('form', 'material', 'color')
    list_filter = ('color', 'material')

class BridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ['color', 'name']

class PickupAdmin(admin.ModelAdmin):
    list_display = ('get_produser', 'set_type', 'type')
    list_filter = ['produser', 'set_type', 'type']
    def get_produser(self, obj):
        return obj.produser.name
    get_produser.admin_order_field  = 'produser'  #Allows column order sorting
    get_produser.short_description = 'Produser'

class GuitarTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']

class GuitarAdmin(admin.ModelAdmin):
    list_display = ('get_produser', 'string_amount', 'get_type')
    list_filter = ['guitar_produser', 'string_amount', 'type']
    def get_type(self, obj):
        return obj.type.name
    get_type.admin_order_field = 'type'
    get_type.short_description = 'Type'
    def get_produser(self, obj):
        return obj.guitar_produser.name
    get_produser.admin_order_field  = 'produser'  #Allows column order sorting
    get_produser.short_description = 'Produser'

admin.site.register(models.Produser, ProduserAdmin)
admin.site.register(models.Body, BodyAdmin)
admin.site.register(models.Bridge, BridgeAdmin)
admin.site.register(models.Pickup, PickupAdmin)
admin.site.register(models.GuitarType, GuitarTypeAdmin)
admin.site.register(models.Guitar, GuitarAdmin)