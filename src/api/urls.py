from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import categories_list, goods_list


urlpatterns = [
    url(r'^categories/$', categories_list),
    url(r'^goods/$', goods_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
