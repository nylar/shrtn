from django.conf.urls import include, url
from links.views import RedirectToView, CreateLinkView, LinkDetailsView


urlpatterns = [
    url(r'^(?P<key>.+)/view/$', LinkDetailsView.as_view(), name='link-details'),
    url(r'^(?P<key>.+)/$', RedirectToView.as_view(), name='redirect-to'),
    url(r'^$', CreateLinkView.as_view(), name='new-link'),
]