from django.contrib import admin
from .models import Category, Product
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, MyAdmin)
admin.site.register(Product)
