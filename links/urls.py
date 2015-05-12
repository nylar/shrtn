from django.conf.urls import include, url
from links.views import RedirectToView, CreateLinkView, LinkDetailsView


urlpatterns = [
    url(r'^(?P<key>.+)/v/$', RedirectToView.as_view(), name='redirect-to'),
    url(r'^(?P<key>.+)/$', LinkDetailsView.as_view(), name='link-details'),
    url(r'^$', CreateLinkView.as_view(), name='new-link'),
]