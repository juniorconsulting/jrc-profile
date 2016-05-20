from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from profiles import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
