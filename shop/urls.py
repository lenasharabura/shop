from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include

from goods.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include(('rest_framework.urls', 'rest'))),
    path('', include(('goods.urls', 'good'))),
    path('', home, name='home')
    # url(r'^showimage/', include('showimage.urls')),
    # url('', include(('social_django.urls', 'social'))),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

