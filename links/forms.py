from django.forms import ModelForm, URLField
from django.utils.translation import ugettext_lazy as _
from links.models import Link


class CreateLinkForm(ModelForm):

    class Meta:
        model = Link
        fields = ['url']
        labels = {
            'url': _(''),
        }
