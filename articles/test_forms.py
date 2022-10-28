from django.test import TestCase
from .forms import ArticleForm, CommentForm


class TestArticleForm(TestCase):
    def test_post_title_is_required(self):
        form = ArticleForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = ArticleForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ArticleForm()
        self.assertEqual(form.Meta.fields, ('title', 'content', 'excerpt',
        'featured_image'))


class TestCommentForm(TestCase):
    def test_post_title_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
