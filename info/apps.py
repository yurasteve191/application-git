import os
from django.apps import AppConfig


class InfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'info'

    def ready(self):
        from .models import TopNews, News
        from django.db.models.signals import post_delete
        from django.dispatch import receiver

        @receiver(post_delete, sender=TopNews)
        def auto_delete_file_on_delete(sender, instance, **kwargs):
            """
            Deletes file from filesystem
            when corresponding `MediaFile` object is deleted.
            """
            if instance.image:
                if os.path.isfile(instance.image.path):
                    os.remove(instance.image.path)

        
        @receiver(post_delete, sender=News)
        def auto_delete_file_on_delete(sender, instance, **kwargs):
            """
            Deletes file from filesystem
            when corresponding `MediaFile` object is deleted.
            """
            if instance.image:
                if os.path.isfile(instance.image.path):
                    os.remove(instance.image.path)