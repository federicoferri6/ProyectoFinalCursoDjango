from django.contrib import admin
from apps.stock.models import Product, Label


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'weight', 'package_type')
    search_fields = ('name', )
    list_filter = (
        'expiracy_date', 'label', 'shipped_date', 'manufactured_date'
    )


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Label, LabelAdmin)
