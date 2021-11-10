from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from goods.models import Product, Category, Feedback


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('slug', 'name', 'image', 'price')


class CategorySerializer(ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=True)
    class Meta:
        model = Category
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class FeedbackSerializer(ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'
