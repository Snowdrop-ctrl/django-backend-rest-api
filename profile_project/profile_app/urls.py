from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profile_app import views

router = DefaultRouter()
router.register('view_set', views.Helloviewset, basename='view_set')

urlpatterns = [
    path('hello/',views.helloview.as_view()),
    path('',include(router.urls)),
]
