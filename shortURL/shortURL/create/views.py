import rest_framework.status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def create_short_url(request):
    print(request)
    if request.method == "POST":

        return HttpResponse("Hello World2", content_type="text/plain", status=rest_framework.status.HTTP_200_OK)
    return HttpResponse("bad request", content_type="text/plain", status=rest_framework.status.HTTP_400_BAD_REQUEST)



