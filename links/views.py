from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView, View
from links.models import Link


class IndexView(View):
    pass


class RedirectToView(RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        key = kwargs.get('key')
        try:
            pk = int(Link.decode(str(key)))
        except ValueError:
            pk = None

        link = get_object_or_404(Link, pk=pk)
        return link.url
