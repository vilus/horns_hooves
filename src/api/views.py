# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['GET'])
def goods_list(_, format=None):
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data)
