from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import TestCase, RequestFactory
from links.models import Link
from links.views import RedirectToView, CreateLinkView


class RedirectToViewTestCase(TestCase):
    """ Tests for the RedirectToView view """

    def setUp(self):
        super(RedirectToViewTestCase, self).setUp()
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


class CreateLinkViewTestCase(TestCase):
    """ Tests for the CreateLinkView view """

    def setUp(self):
        super(CreateLinkViewTestCase, self).setUp()
        self.factory = RequestFactory()

    def test_form_redirects_to_link_details_page(self):
        request = self.factory.post(reverse('new-link'), data={'url': 'http://example.com'})
        response = CreateLinkView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/MQ==/')
