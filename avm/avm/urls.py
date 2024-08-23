from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from dm import views as dm_views


router = routers.DefaultRouter()
router.register(r"dm", dm_views.DmViewSet, basename="dm")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
