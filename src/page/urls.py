from django.conf.urls import url
from page import views


urlpatterns = [
    url(r'^(?:(?P<category_id>\d+)/)?$', views.index, name='page_index'),
    url(r'^good/(?P<good_id>\d+)/$', views.good, name='good')
]
