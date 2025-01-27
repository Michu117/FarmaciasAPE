from django.contrib import admin
from .models import (Farmacia, Sucursal, Medicamento, Inventario, Cliente, Empleado, Factura, ItemFactura,
                     Transferencia)

@admin.register(Farmacia)
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields =( 'nombre', 'direccion', 'telefono')
    list_filter =( 'nombre', 'direccion', 'telefono')
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('numeroSucursal', 'direccion', 'telefono', 'farmacia')
    search_fields = ('numeroSucursal', 'direccion', 'telefono', 'farmacia')
    list_filter = ('numeroSucursal', 'direccion', 'telefono', 'farmacia')
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre', 'precio')
    list_filter = ('nombre', 'precio')
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'medicamento', 'cantidad')
    search_fields = ('sucursal', 'medicamento', 'cantidad')
    list_filter = ('sucursal', 'medicamento', 'cantidad')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'telefono', 'email')
    search_fields = ('nombre', 'cedula', 'telefono', 'email')
    list_filter = ('nombre', 'cedula', 'telefono', 'email')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'sucursal', 'rol')
    search_fields = ('nombre', 'cedula', 'sucursal', 'rol')
    list_filter = ('nombre', 'cedula', 'sucursal', 'rol')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numeroFactura', 'fecha', 'cliente', 'sucursal', 'total', 'metodoPago')
    search_fields = ('numeroFactura', 'fecha', 'cliente', 'sucursal', 'total', 'metodoPago')
    list_filter = ('numeroFactura', 'fecha', 'cliente', 'sucursal', 'total', 'metodoPago')

@admin.register(ItemFactura)
class ItemFacturaAdmin(admin.ModelAdmin):
    list_display = ('numeroitemfactura', 'factura', 'medicamento', 'cantidad')
    search_fields = ('numeroitemfactura', 'factura', 'medicamento', 'cantidad')
    list_filter = ('numeroitemfactura', 'factura', 'medicamento', 'cantidad')

@admin.register(Transferencia)
class TransferenciaAdmin(admin.ModelAdmin):
    list_display = ('numero_transferencia', 'medicamento', 'sucursal_origen', 'sucursal_destino', 'cantidad', 'fecha', 'estado')
    search_fields = ('numero_transferencia', 'medicamento', 'sucursal_origen', 'sucursal_destino', 'cantidad', 'fecha', 'estado')
    list_filter = ('numero_transferencia', 'medicamento', 'sucursal_origen', 'sucursal_destino', 'cantidad', 'fecha', 'estado')


