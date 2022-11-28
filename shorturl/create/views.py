import json
import rest_framework.status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import insert_to_db


@csrf_exempt
def create_short_url(request) -> HttpResponse:
    if request.method == "POST" and request.content_type == "application/json":
        params = request.read()
        data = json.loads(params.decode('utf8').replace("'", '"'))

        try:
            url = data['url']
            if ("http://" not in url) and ("https://" not in url):
                url = "http://" + url
        except:
            return HttpResponse("url parameter is missing",
                                content_type="text/plain",
                                status=rest_framework.status.HTTP_400_BAD_REQUEST)
        return insert_to_db(url)
    else:
        return HttpResponse("bad request", content_type="text/plain", status=rest_framework.status.HTTP_400_BAD_REQUEST)
