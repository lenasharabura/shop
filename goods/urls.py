from django.urls import path
from rest_framework.routers import DefaultRouter

from goods.views import *

router = DefaultRouter()
router.register(r'api/products_list/<slug:slug>', ProductDetailView)
router.register(r'api/category', CategoryListView)
router.register(r'api/products_list', ProductsListView)
router.register(r'api/<slug:slug>', CategoryDetailView)


urlpatterns = router.urls
