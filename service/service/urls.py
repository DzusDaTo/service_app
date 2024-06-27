from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from services.views import SubscriptionView


router = routers.DefaultRouter()
router.register(r'api/subscription', SubscriptionView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]



