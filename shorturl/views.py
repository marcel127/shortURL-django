from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from shorturl.models import URLEntry
import rest_framework.status


@csrf_exempt
def redirect_url(request, short_url):
    try:
        url_details = URLEntry.objects.get(unique_id=short_url)
        url_details.count = url_details.count + 1
        URLEntry.save()
    except:
        return HttpResponse(f"bad request, http://localhost/{short_url}, does not exist"
                            , content_type="text/plain", status=rest_framework.status.HTTP_404_NOT_FOUND)

    return redirect(url_details.original_url)



