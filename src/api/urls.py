from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import CategoryList, CategoryAdd, CategoryDel, CategoryUpdate, CategoryDetail
from api.views import GoodList, GoodDetail, GoodAdd, GoodDel, GoodUpdate


urlpatterns = [
    url(r'^categories/$', CategoryList.as_view(), name='categories_list'),
    url(r'^categories/add/$', CategoryAdd.as_view(), name='category_add'),
    url(r'^categories/(?P<pk>\d+)/delete/$', CategoryDel.as_view(), name='category_del'),
    url(r'^categories/(?P<pk>\d+)/update/$', CategoryUpdate.as_view(), name='category_update'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^goods/$', GoodList.as_view(), name='good_list'),
    url(r'^goods/(?P<pk>\d+)/$', GoodDetail.as_view(), name='good_detail'),
    url(r'^goods/add/$', GoodAdd.as_view(), name='good_add'),
    url(r'^goods/(?P<pk>\d+)/delete/$', GoodDel.as_view(), name='good_del'),
    url(r'^goods/(?P<pk>\d+)/update/$', GoodUpdate.as_view(), name='good_update'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
