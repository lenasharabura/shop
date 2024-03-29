from django.urls import path
from rest_framework.routers import DefaultRouter

from goods.views import *


urlpatterns = [
    path('api/feedback/', FeedbackView.as_view(), name='feedback'),
    path('api/products_list/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('api/category/', CategoryListView.as_view(), name='home_page'),
    path('api/products_list/', ProductsListView.as_view(), name='products_list'),


    path('api/<slug:slug>/', CategoryDetailView.as_view(), name='category_product'),


]
