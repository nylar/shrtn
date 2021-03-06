from base64 import urlsafe_b64encode, urlsafe_b64decode
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Link(models.Model):
    url = models.URLField()
    key = models.CharField(max_length=25)

    def encode(self):
        return urlsafe_b64encode(str(self.id))

    @classmethod
    def decode(cls, key):
        # Values should be in 4 byte segments, otherwise an exception is thrown.
        segment_size = len(key) % 4

        if segment_size:
            # Pad the key with '=' to make it a mutiple of 4.
            key += '='*segment_size

        return urlsafe_b64decode(key)

    def __unicode__(self):
        return self.key


@receiver(post_save, sender=Link)
def generate_key(sender, instance, created, **kwargs):
    if created:
        instance.key = instance.encode()
