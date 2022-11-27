# $ curl -X POST "http://localhost:8000/create" \
# -H "Content-Type: application/json" \
# -d '{"url": "https://ravkavonline.co.il"}'
# http://localhost:8000/s/slKj289

from django.db import models


class URLEntry(models.Model):
    url = models.URLField()
    unique_id = models.SlugField(max_length=6, primary_key=True, blank=True)
    count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    shortened_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

