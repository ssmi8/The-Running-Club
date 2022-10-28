from django.test import TestCase
from .models import Post


class TestModels(TestCase):
    def test_has_featured_image(self):
        self.asserTrue(Post.featured_image)
