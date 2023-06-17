from django.contrib import admin
from.models import Product

class ProductAdmin(admin.modelAdmin):
    list_display("name","store","price","date_craeted")
Admin.register(Product,ProductAdmin)



# Register your models here.
