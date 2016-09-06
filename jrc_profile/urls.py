from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from profiles import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^profiles/$', views.profile_list),
    url(r'^profiles-all/$', views.profile_list_get),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.profile_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
