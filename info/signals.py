from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

from info.models import TopNews

@receiver(post_delete, sender=TopNews)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)