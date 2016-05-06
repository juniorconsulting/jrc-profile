from django.conf.urls import url, include
from rest_framework import routers

from profiles import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
