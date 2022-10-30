from django.test import TestCase, Client
from .models import Post
from django.urls import reverse


class TestIndexViews(TestCase):
    """Unit Test Index Page View"""
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
