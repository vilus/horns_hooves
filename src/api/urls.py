from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import api.views as controllers


urlpatterns = [
    url(r'^categories/$', controllers.categories_list),
    url(r'^categories/add/$', controllers.categories_add),
    url(r'^categories/(?P<pk>\d+)/delete/$', controllers.categories_del),
    url(r'^categories/(?P<pk>\d+)/update/$', controllers.categories_update),
    url(r'^goods/$', controllers.goods_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
