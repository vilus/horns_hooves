# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(req, category_id):
    return HttpResponse('there is index or content of %s category' % category_id)


def good(req, good_id):
    return HttpResponse('there is %s good' % good_id)
