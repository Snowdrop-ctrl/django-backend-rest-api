from django.urls import path
from profile_app import views


urlpatterns = [
    path('hello/',views.helloview.as_view())
]
