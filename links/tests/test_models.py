from django.test import TestCase
from links.models import Link


class LinkModelTestCase(TestCase):
    """ Tests for the link model """
    
    def test_link(self):
        l = Link.objects.create(url='http://google.com')
        self.assertEqual(l.url, 'http://google.com')
        self.assertEqual(l.key, 'MQ==')

        self.assertEqual(Link.objects.count(), 1)

    def test_link_unicode(self):
        l = Link.objects.create(url='http://google.com')
        self.assertEqual(str(l), 'MQ==')

    def test_link_encode(self):
        tests = [
            (1, 'MQ=='),
            (100, 'MTAw'),
            (10000, 'MTAwMDA='),
            (1000000, 'MTAwMDAwMA=='),
        ]

        for test in tests:
            l = Link(id=test[0], url='http://example.com')
            key = l.encode()
            self.assertEqual(key, test[1])

    def test_link_decode(self):
        tests = [
            ('MTIzNDU2Nzg5', '123456789'),
            ('OTk5', '999'),
            ('MTIyMzMzNDQ0NDU1NTU1', '122333444455555'),
        ]

        for test in tests:
            pk = Link.decode(test[0])
            self.assertEqual(pk, test[1])

    def test_link_decode_pads_keys(self):
        key = 'xx'
        pk = Link.decode(key)
        self.assertEqual(pk, '\xc7')
