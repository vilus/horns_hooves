# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response
from page.models import Category, Good
from api.serializers import CategorySerializer, GoodSerializer


@api_view(['GET'])
def categories_list(_, format=None):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def goods_list(_, format=None):
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data)
