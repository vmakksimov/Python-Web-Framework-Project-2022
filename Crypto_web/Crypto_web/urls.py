"""Crypto_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('Crypto_web.web.urls')),
                  path('accounts/', include('Crypto_web.accounts.urls')),
                  path('news/', include('Crypto_web.news.urls')),
                  path('article/', include('Crypto_web.helparticle.urls')),
                  path('event/', include('Crypto_web.event.urls')),
                  path('partners/', include('Crypto_web.partners.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'Crypto_web.common.custom_errors_handling.handler400'
handler404 = 'Crypto_web.common.custom_errors_handling.handler404'
handler403 = 'Crypto_web.common.custom_errors_handling.handler403'
handler500 = 'Crypto_web.common.custom_errors_handling.handler500'

