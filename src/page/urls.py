from django.conf.urls import url
from page.cviews import GoodListView, GoodDetailView


urlpatterns = [
    url(r'^(?:(?P<category_id>\d+)/)?$', GoodListView.as_view(), name='page_index'),
    url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name='good')
]
