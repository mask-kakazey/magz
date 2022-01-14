from django.db.models import Count
from rest_framework import generics

from .models import Product, Category
from .serializers import ProductListSerializer, CategoryListSerializer, ProductDetailSerializer


class CategoryProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        category = Category.objects.get(pk=category_id)
        products_id = category.get_descendants().prefetch_related('products').values_list('products', flat=True)
        product = Product.objects.filter(pk__in=products_id)
        return product


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
