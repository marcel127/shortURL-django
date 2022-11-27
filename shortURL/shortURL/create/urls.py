from django.urls import path
from .views import create_short_url

urlpatterns = [
    path("", create_short_url, name="create_short_url"),
]
