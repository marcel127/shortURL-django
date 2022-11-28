from django.db import models


class URLEntry(models.Model):
    # unique_id it's actually the suffix of the short url and the primary_key
    unique_id = models.SlugField(max_length=10, primary_key=True, blank=True)
    # the original url that the user provide
    original_url = models.URLField()
    # count number of enters starting from zero
    count = models.IntegerField(default=0)
    # only for the order of the db table
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]
