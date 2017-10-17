# coding=utf-8
import logging
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import ContextMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from page.models import Category, Good

logger = logging.getLogger('dev.'+__name__)


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context['cats'] = Category.objects.order_by('name')
        return context


class GoodEditMixin(CategoryListMixin):
    def get_context_data(self, **kwargs):
        context = super(GoodEditMixin, self).get_context_data(**kwargs)
        context['pn'] = self.request.GET.get('page', 1)
        return context


class GoodEditView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        pn = request.GET.get('page', '1')
        self.success_url = self.success_url + '?page=' + pn
        return super(GoodEditView, self).post(request, *args, **kwargs)


class GoodCreate(SuccessMessageMixin, CreateView, GoodEditMixin):
    model = Good
    template_name = 'page/page_good_add.html'
    fields = '__all__'
    success_message = 'Товар успешно добавлен'

    def get(self, request, *args, **kwargs):
        if self.kwargs['cat_id'] is not None:
            try:
                cat_id = int(self.kwargs['cat_id'])
            except ValueError:
                raise Http404()
            self.initial['category'] = get_object_or_404(Category, pk=cat_id)
        return super(GoodCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        cat_id = Category.objects.get(pk=self.kwargs['cat_id']).id
        self.success_url = reverse('page_index', kwargs={'cat_id': cat_id})
        return super(GoodCreate, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodCreate, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['cat_id'])
        return context


class GoodUpdate(SuccessMessageMixin, UpdateView, GoodEditMixin, GoodEditView):
    model = Good
    template_name = 'page/page_good_edit.html'
    pk_url_kwarg = 'good_id'
    fields = '__all__'
    success_message = 'Товар успешно изменен'

    def post(self, request, *args, **kwargs):
        cat_id = Good.objects.get(pk=kwargs['good_id']).category.id
        self.success_url = reverse('page_index', kwargs={'cat_id': cat_id})
        return super(GoodUpdate, self).post(request, *args, **kwargs)


class GoodDelete(DeleteView, GoodEditMixin, GoodEditView):
    model = Good
    template_name = 'page/page_good_delete.html'
    pk_url_kwarg = 'good_id'
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        # TODO: seems like *View already reraise DoesNotExists to Http404
        cat_id = Good.objects.get(pk=kwargs['good_id']).category.id
        self.success_url = reverse('page_index', kwargs={'cat_id': cat_id})
        return super(GoodDelete, self).post(request, *args, **kwargs)


class GoodListView(ListView, CategoryListMixin):
    template_name = 'page/page_index.html'
    paginate_by = 3
    cat = None

    def get(self, request, *args, **kwargs):
        if kwargs['cat_id']:
            self.cat = get_object_or_404(Category, id=kwargs['cat_id'])
        else:
            self.cat = Category.objects.first()
        if self.cat:
            logger.debug('get goods for category: {0}'.format(self.cat.name))
        return super(GoodListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        return context

    def get_queryset(self):
        goods = Good.objects.filter(category=self.cat).order_by('name')
        tag = self.request.GET.get('tag')
        if tag:
            goods = goods.filter(tags__name=tag)
        return goods


class GoodDetailView(DetailView, CategoryListMixin):
    template_name = 'page/page_good.html'
    model = Good
    pk_url_kwarg = 'good_id'

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        context['pn'] = self.request.GET.get('page', 1)
        return context
