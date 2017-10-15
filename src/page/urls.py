from django.conf.urls import url
from django.contrib.auth.decorators import permission_required
from page.cviews import GoodListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete


urlpatterns = [
    url(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name='page_index'),
    url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name='good'),
    url(r'^(?P<cat_id>\d*)/add/$',
        permission_required('page.add_good')(GoodCreate.as_view()), name='good_add'),
    url(r'^good/(?P<good_id>\d+)/edit/$',
        permission_required('page.change_good')(GoodUpdate.as_view()), name='good_edit'),
    url(r'^good/(?P<good_id>\d+)/delete/$',
        permission_required('page.delete_good')(GoodDelete.as_view()), name='good_delete'),
]
