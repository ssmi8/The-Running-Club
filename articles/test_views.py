from django.test import TestCase
from .models import Post


class TestIndexViews(TestCase):
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestArticlsViews(TestCase):
    def test_get_articles_page(self):
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')


class TestPublishViews(TestCase):
    def test_publish_page(self):
        response = self.client.get('/publish')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish.html')


class TestProfileViews(TestCase):
    def test_profile_page(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

