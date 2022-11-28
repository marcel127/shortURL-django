from django.urls import path, include
from .views import redirect_url

app_name = 'shorturl'

urlpatterns = [
    path("create", include("shorturl.create.urls")),
    path("", redirect_url, name="redirect_url"),

]
