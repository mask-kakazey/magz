from django.db import models
from django.urls import reverse
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


class Product(models.Model):
    name = models.CharField('Товар', max_length=50)
    description = models.TextField('Описание')
    scope_of_application = models.CharField('Сфера приминения', max_length=150)
    diameter = models.CharField('Диаметр', max_length=150)
    length = models.CharField('Длина', max_length=150)
    color = models.CharField('Цвет', max_length=50)
    image = models.ImageField('Изображение', upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
