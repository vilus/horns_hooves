# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage
from page.models import Category, Good


def index(req, category_id):
    cats = Category.objects.all().order_by('name')
    cat = Category.objects.get(pk=category_id) if category_id else Category.objects.first()
    goods = Good.objects.filter(category=cat).order_by('name')
    paginator = Paginator(goods, 4)
    goods = paginator.page(req.GET.get('page', 1))
    return render(req, 'page_index.html', {'category': cat, 'cats': cats, 'goods': goods})


def good(req, good_id):
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    pn = req.GET.get('page', 1)
    return render(req, 'page_good.html', {'good': good, 'cats': cats, 'pn': pn})
