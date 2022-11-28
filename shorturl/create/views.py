import json
import rest_framework.status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import insert_to_db


@csrf_exempt
def create_short_url(request) -> HttpResponse:
    # check if the request is a post request and had a json content type, if no return bad request
    if request.method == "POST" and request.content_type == "application/json":
        # parsing the params
        params = request.read()
        data = json.loads(params.decode('utf8').replace("'", '"'))

        try:
            url = data['url']
            # if the user forgot the prefix of http/https we add
            if ("http://" not in url) and ("https://" not in url):
                url = "http://" + url
        except:
            # if no url parameter in the json
            return HttpResponse("url parameter is missing",
                                content_type="text/plain",
                                status=rest_framework.status.HTTP_400_BAD_REQUEST)

        return insert_to_db(url)
    else:
        return HttpResponse("bad request", content_type="text/plain", status=rest_framework.status.HTTP_400_BAD_REQUEST)
