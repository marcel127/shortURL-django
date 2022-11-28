import rest_framework.status
import uuid
from shorturl.models import URLEntry
from django.http import HttpResponse


def insert_to_db(original_url):
    try:
        # generate unique id, and then insert to db,
        # if the operation not succeed return 304 not modified, else return the short url
        unique_id = generate_unique_id()
        entry = URLEntry(original_url=original_url, unique_id=unique_id)
        entry.save()
    except:
        return HttpResponse("something gone wrong", content_type="text/plain",
                            status=rest_framework.status.HTTP_304_NOT_MODIFIED)

    return HttpResponse(f"http://localhost:8000/{unique_id}",
                        content_type="text/plain",
                        status=rest_framework.status.HTTP_200_OK)


def generate_unique_id() -> str:
    # create uid until is not exist on db
    uid = str(uuid.uuid4())[:12]
    try:
        while True:
            URLEntry.objects.get(unique_id=uid)
            uid = str(uuid.uuid4())[:12]

    except:
        return uid
