from django.shortcuts import render
from django.views.generic import UpdateView

from rest_framework import status, permissions, mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, GenericAPIView

__all__ = (
    'CategoryListView',
    'ProductsListView',
    'ProductDetailView',
    'CategoryDetailView',
    'FeedbackView',
)

from rest_framework.parsers import JSONParser, MultiPartParser

from rest_framework.response import Response

from goods.models import Category, Product, Feedback
from goods.serializers import CategorySerializer, ProductListSerializer, ProductDetailSerializer, FeedbackSerializer


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


class FeedbackView(mixins.CreateModelMixin, GenericAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    parser_classes = (JSONParser, MultiPartParser, )

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)