from django.urls import path, include
from .views import redirect_url

app_name = 'shorturl'

urlpatterns = [
    path("create", include("shorturl.create.urls")),
    path("<str:short_url>", redirect_url, name="redirect_url"),

]
