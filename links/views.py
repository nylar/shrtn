from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from links.forms import CreateLinkForm
from links.models import Link


class LinkDecoderMixin(object):

    def get_pk_from_key(self, key):
        try:
            pk = int(Link.decode(str(key)))
        except ValueError:
            pk = None
        return pk


class CreateLinkView(CreateView):
    model = Link
    form_class = CreateLinkForm

    def get_success_url(self):
        return reverse('link-details', kwargs={'key': self.object.key}) 


class LinkDetailsView(LinkDecoderMixin, DetailView):
    model = Link
    pk_url_kwarg = 'key'

    def get_object(self):
        key = self.kwargs.get('key')
        pk = self.get_pk_from_key(key)
        return Link.objects.get(pk=pk)


class RedirectToView(LinkDecoderMixin, RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        key = kwargs.get('key')
        pk = self.get_pk_from_key(key)
        link = get_object_or_404(Link, pk=pk)
        return link.url
