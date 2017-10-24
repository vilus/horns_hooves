# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, mixins
from page.models import Category, Good
from api.serializers import CategorySerializer, GoodSerializer


class SetChangedByMixin(object):
    def set_changed_by(self, serializer):
        serializer.save(changed_by=self.request.user)


class CategotyAPIView(SetChangedByMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(mixins.ListModelMixin, CategotyAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryAdd(mixins.CreateModelMixin, CategotyAPIView):
    def perform_create(self, serializer):
        self.set_changed_by(serializer)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDel(mixins.DestroyModelMixin, CategotyAPIView):
    def perform_destroy(self, instance):
        instance.changed_by = self.request.user
        super(CategoryDel, self).perform_destroy(instance)

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryUpdate(mixins.UpdateModelMixin, CategotyAPIView):
    def perform_update(self, serializer):
        self.set_changed_by(serializer)

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CategoryDetail(mixins.RetrieveModelMixin, CategotyAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GoodAPIView(SetChangedByMixin, generics.GenericAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodList(mixins.ListModelMixin, GoodAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GoodDetail(mixins.RetrieveModelMixin, GoodAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GoodAdd(mixins.CreateModelMixin, GoodAPIView):
    def perform_create(self, serializer):
        self.set_changed_by(serializer)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GoodDel(mixins.DestroyModelMixin, GoodAPIView):
    def perform_destroy(self, instance):
        instance.changed_by = self.request.user
        super(GoodDel, self).perform_destroy(instance)

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GoodUpdate(mixins.UpdateModelMixin, GoodAPIView):
    def perform_update(self, serializer):
        self.set_changed_by(serializer)

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
