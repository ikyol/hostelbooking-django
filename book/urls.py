from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('', include('main.urls')),
    path('', MainPageView.as_view(), name='homepage'),
    path('accounts/', include('user.urls')),
    path('captcha', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
