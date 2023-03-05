from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/info/', include('info.urls')),
    path('api/support/', include('support.urls')),
    path('api/menu/',include('menu.urls')),

    path('', TemplateView.as_view(template_name='index.html'), name='index')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
