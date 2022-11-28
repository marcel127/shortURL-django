import rest_framework.status
import uuid
from shorturl.models import URLEntry
from django.http import HttpResponse


# 'd20a8513-b'

def insert_to_db(original_url):
    try:
        unique_id = generate_unique_id()
        entry = URLEntry(original_url=original_url, unique_id=unique_id)
        entry.save()
    except:
        return HttpResponse("something gone wrong", content_type="text/plain",
                            status=rest_framework.status.HTTP_400_BAD_REQUEST)

    return HttpResponse(f"http://localhost:8000/{unique_id}\n",
                        content_type="text/plain",
                        status=rest_framework.status.HTTP_200_OK)


def generate_unique_id() -> str:
    uid = str(uuid.uuid4())[:10]
    try:
        while True:
            URLEntry.objects.get(unique_id=uid)
            uid = str(uuid.uuid4())[:10]

    except:
        return uid
