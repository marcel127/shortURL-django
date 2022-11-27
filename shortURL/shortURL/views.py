from http.client import HTTPResponse

import django
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

from django.http import HttpResponseRedirect


@csrf_exempt
def redirect_url(request):
    if request.method == "POST":
        return HttpResponse("Hello World2", content_type="text/plain", status=200)
    return HttpResponse("bad request", content_type="text/plain", status=400)



