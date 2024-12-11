from django.contrib import admin
from product.models import Brand, ParentCategory, Category, Product, ProductImages, Subcategory, BrandWithImage, Filter, FilterValue
from product.forms import ProductModelAdminForm


class ProductModelAdmin(admin.ModelAdmin):
    form = ProductModelAdminForm


admin.site.register(Brand)
admin.site.register(ParentCategory)
admin.site.register(Category)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductImages)
admin.site.register(Subcategory)
admin.site.register(BrandWithImage)
admin.site.register(Filter)
admin.site.register(FilterValue)
