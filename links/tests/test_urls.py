from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from links.models import Link


class LinkUrlsTestCase(TestCase):
    """ Tests for the links.urls """

    def setUp(self):
        super(LinkUrlsTestCase, self).setUp()
        self.client = Client()

    def test_redirect_url(self):
        l = Link.objects.create(url="http://example.com/")
        response = self.client.get(reverse('redirect-to', kwargs={'key': l.key}))
        self.assertEqual(response.status_code, 301)
