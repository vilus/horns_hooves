from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import api.views as controllers
from api.views import CategoryList, CategoryAdd, CategoryDel, CategoryUpdate, CategoryDetail


urlpatterns = [
    url(r'^categories/$', CategoryList.as_view(), name='categories_list'),
    url(r'^categories/add/$', CategoryAdd.as_view(), name='category_add'),
    url(r'^categories/(?P<pk>\d+)/delete/$', CategoryDel.as_view(), name='category_del'),
    url(r'^categories/(?P<pk>\d+)/update/$', CategoryUpdate.as_view(), name='category_update'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^goods/$', controllers.goods_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
