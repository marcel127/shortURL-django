from django.db import models


class URLEntry(models.Model):
    unique_id = models.SlugField(max_length=10, primary_key=True, blank=True)
    original_url = models.URLField()
    count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]
