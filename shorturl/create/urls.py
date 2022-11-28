from django.urls import path
from .views import create_short_url

app_name = 'shorturl'


urlpatterns = [
    path("", create_short_url, name="create_short_url"),
]
