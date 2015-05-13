import requests

from django import template


register = template.Library()


@register.assignment_tag
def check(url):
    # Assume the URL is unreachable
    reachable = False

    try:
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            reachable = True
    except requests.ConnectionError:
        pass

    return reachable
