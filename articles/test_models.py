from django.test import TestCase
from .models import Post


class TestModels(TestCase):
    def test_has_featured_image(self):
        self.assertTrue(Post.featured_image)
