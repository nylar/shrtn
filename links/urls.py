from django.conf.urls import include, url
from links.views import RedirectToView, IndexView


urlpatterns = [
    url(r'^(?P<key>.+)', RedirectToView.as_view(), name='redirect-to'),
    url(r'^$', IndexView.as_view(), name='index'),
]