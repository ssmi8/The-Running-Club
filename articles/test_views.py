from django.test import TestCase
from .models import Post


class TestIndexViews(TestCase):
    """Unit Test Index Page View"""
    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestPostListViews(TestCase):
    """Unit Test Post List Page View"""
    def test_get_post_list_page(self):
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')


class TestProfileViews(TestCase):
    """Unit Test Profile Page View"""
    def test_profile_page(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class TestPublishPoemViews(TestCase):
    """Unit Test Publish Page View"""
    def test_can_publish_poem(self):
        response = self.client.get('/publish')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish.html')
