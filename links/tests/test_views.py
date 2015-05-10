from django.http import Http404
from django.test import TestCase, RequestFactory
from links.models import Link
from links.views import RedirectToView


class RedirectToTestCase(TestCase):
    """ Tests for the RedirectTo view """

    def setUp(self):
        super(RedirectToTestCase, self).setUp()
        self.factory = RequestFactory()
        self.link = Link.objects.create(url="http://example.com")

    def test_redirects_successfully(self):
        request = self.factory.get('/')
        response = RedirectToView.as_view()(request, key=self.link.key)
        self.assertEqual(response.status_code, 301)

    def test_redirect_to_404s_with_bad_key(self):
        request = self.factory.get('/')
        with self.assertRaises(Http404):
            RedirectToView.as_view()(request, key='xx')
