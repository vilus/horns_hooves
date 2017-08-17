from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from page.models import Category, Good


class GoodListView(TemplateView):
    template_name = 'page_index.html'

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)

        context['cats'] = Category.objects.all().order_by('name')
        if kwargs['category_id']:
            context['category'] = Category.objects.get(id=kwargs['category_id'])
        else:
            context['category'] = Category.objects.first()

        goods = Good.objects.filter(category=context['category']).order_by('name')
        paginator = Paginator(goods, 4)
        try:
            context['goods'] = paginator.page(self.request.GET.get('page', 1))
        except InvalidPage:
            context['goods'] = paginator.page(1)

        return context


class GoodDetailView(TemplateView):
    template_name = 'page_good.html'

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.all().order_by("name")
        try:
            context['good'] = Good.objects.get(pk=kwargs['good_id'])
        except Good.DoesNotExist:
            raise Http404
        context['pn'] = self.request.GET.get('page', 1)
        return context
