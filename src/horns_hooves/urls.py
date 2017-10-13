"""horns_hooves URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.flatpages.views import flatpage
from page.models import Category


urlpatterns = []

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^dbg/', include(debug_toolbar.urls, namespace='djdt')))

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login,
        {'template_name': 'page/login.html', 'extra_context': {'cats': Category.objects.all()}}, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^goods/', include('page.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^(?P<url>.*/)$', flatpage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
