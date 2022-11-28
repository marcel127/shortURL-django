from django.test import RequestFactory, TestCase
from django.test import Client


class SimpleTest(TestCase):

    def test_create_and_redirect(self):
        c = Client()
        response = c.post('http://localhost:8000/create', content_type="application/json", data={"url": "google.com"})
        assert response.status_code == 200

        url = response.content.decode("utf-8")
        response = c.get(url)
        assert response.status_code < 400

    def test_url_spelling_missing(self):
        c = Client()
        response = c.post('http://localhost:8000/create', content_type="application/json", data={"l": "google.com"})
        assert response.status_code != 200

    def test_no_url_missing(self):
        c = Client()
        response = c.post('http://localhost:8000/create', content_type="application/json")
        assert response.status_code != 200

    def test_not_exist_url(self):
        c = Client()
        response = c.post('http://localhost:8000/create', content_type="application/json", data={"url": "google.com"})
        assert response.status_code == 200

        url = response.content.decode("utf-8")
        response = c.get(url + "2132")
        assert response.status_code == 404

    def test_count(self):
        c = Client()
        response = c.post('http://localhost:8000/create', content_type="application/json", data={"url": "google.com"})
        assert response.status_code == 200

        url = response.content.decode("utf-8")
        for i in range(6):
            c.get(url)

        unique_id = url.rsplit('/', 1)[1]
        response = c.get(f'http://localhost:8000/info/{unique_id}')
        breakpoint()
        assert "had 6 clicks" in response.content.decode("utf-8")
