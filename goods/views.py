from django.shortcuts import render
from requests import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

__all__ = (
    'CategoryListView',
    'ProductsListView',
    'ProductDetailView',
    'CategoryDetailView',
    'home'
)

from goods.models import Category, Product
from goods.serializers import CategorySerializer, ProductListSerializer, ProductDetailSerializer


def home(request):
    return render(request, 'index.html')


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    lookup_field = 'slug'


class CategoryDetailView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug=self.kwargs['slug'], available=True)