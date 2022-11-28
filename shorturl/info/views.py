import json
import rest_framework.status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from shorturl.models import URLEntry


@csrf_exempt
def get_count(request, unique_id):
    try:
        # check if the short url exist if exist , increment by one, else return http response not found
        url_details = URLEntry.objects.get(unique_id=unique_id)
        return HttpResponse(f"http://localhost:8000/{unique_id}, had {url_details.count} clicks"
                     , content_type="text/plain", status=rest_framework.status.HTTP_200_OK)
    except:
        return HttpResponse(f"bad request, {unique_id}, does not exist"
                            , content_type="text/plain", status=rest_framework.status.HTTP_404_NOT_FOUND)
