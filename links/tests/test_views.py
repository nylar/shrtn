import responses

from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import TestCase, RequestFactory
from links.models import Link
from links.views import RedirectToView, CreateLinkView, LinkDetailsView
from requests.exceptions import ConnectionError


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

    @responses.activate
    def test_form_redirects_to_link_details_page(self):
        responses.add(responses.GET, 'http://example.com', status=200)

        request = self.factory.post(reverse('new-link'), data={
            'url': 'http://example.com'})
        response = CreateLinkView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/MQ==/')


class LinkDetailsViewTestCase(TestCase):
    """ Tests for the LinkDetailsView view """

    def setUp(self):
        super(LinkDetailsViewTestCase, self).setUp()
        self.factory = RequestFactory()

    @responses.activate
    def test_details_page_with_url_that_is_reachable(self):
        link = Link.objects.create(url="http://example.com")
        responses.add(responses.GET, link.url, status=200)

        request = self.factory.get('/')
        response = LinkDetailsView.as_view()(request, key=link.key)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn('Reachable', response.content)

    @responses.activate
    def test_details_page_with_url_that_is_unreachable(self):
        link = Link.objects.create(url="http://example.com")

        exception = ConnectionError('Can\'t reach URL')
        responses.add(responses.GET, link.url, body=exception)

        request = self.factory.get('/')
        response = LinkDetailsView.as_view()(request, key=link.key)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn('Unreachable', response.content)
