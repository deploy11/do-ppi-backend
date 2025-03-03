# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet,ContactViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('api/', include(router.urls)),
]