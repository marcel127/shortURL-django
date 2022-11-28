from django.urls import path
from .views import get_count

app_name = 'shorturl'


urlpatterns = [
    path("<str:unique_id>", get_count, name="get_count"),
]
