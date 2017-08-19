from django.conf.urls import url
from page.cviews import GoodListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete


urlpatterns = [
    url(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name='page_index'),
    url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name='good'),
    url(r'^(?P<cat_id>\d+)/add/$', GoodCreate.as_view(), name='good_add'),
    url(r'^good/(?P<good_id>\d+)/edit/$', GoodUpdate.as_view(), name='good_edit'),
    url(r'^good/(?P<good_id>\d+)/delete/$', GoodDelete.as_view(), name='good_delete'),
]