from django.contrib import admin
from gadgets.models import Manufacturer, Product, ProductCategory

admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(ProductCategory)
