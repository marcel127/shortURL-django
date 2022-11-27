from django.urls import path, include
from .views import redirect_url


urlpatterns = [
    path("create", include("shortURL.create.urls")),
    path("", redirect_url, name="redirect_url"),

]
