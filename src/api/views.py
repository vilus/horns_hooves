# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, mixins
from page.models import Category, Good
from api.serializers import CategorySerializer, GoodSerializer


class CategotyAPIView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(mixins.ListModelMixin, CategotyAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryAdd(mixins.CreateModelMixin, CategotyAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDel(mixins.DestroyModelMixin, CategotyAPIView):
    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryUpdate(mixins.UpdateModelMixin, CategotyAPIView):
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CategoryDetail(mixins.RetrieveModelMixin, CategotyAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GoodAPIView(generics.GenericAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodList(mixins.ListModelMixin, GoodAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GoodDetail(mixins.RetrieveModelMixin, GoodAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GoodAdd(mixins.CreateModelMixin, GoodAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GoodDel(mixins.DestroyModelMixin, GoodAPIView):
    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GoodUpdate(mixins.UpdateModelMixin, GoodAPIView):
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
