# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.test import TestCase


class SmokeTestCase(TestCase):
    """
    Just check status code of app urls
    """

    fixtures = ['test_data.json']
    urls = [
        {'viewname': 'page_index', 'kwargs': {'cat_id': 1}},
        {'viewname': 'good', 'kwargs': {'good_id': 1}},
        {'viewname': 'good_add', 'kwargs': {'cat_id': 2}},
        {'viewname': 'good_edit', 'kwargs': {'good_id': 1}},
        {'viewname': 'good_delete', 'kwargs': {'good_id': 1}},
    ]

    def setUp(self):
        self.client.post('/login/', {'username': 'qa_staff', 'password': '!1q2w3e4R'})

    def _check_status200(self, **reverse_params):
        check_url = reverse(**reverse_params)
        print('check status of url: {0}'.format(check_url))
        res = self.client.get(check_url)
        self.assertEqual(res.status_code, 200)

for rev_params in SmokeTestCase.urls:
    setattr(SmokeTestCase, 'test_' + rev_params['viewname'], lambda self, x=rev_params: self._check_status200(**x))


class FromMiddlewareCase(TestCase):
    """
    Check cookie that set via process_request and process_responce in middleware
    """

    def test_cookie_from_middleware(self):
        res = self.client.get('/')
        from_md = res.cookies.get('from_middleware', False)
        self.assertTrue(from_md, 'cookie "from_middleware" was not added as expected')
        self.assertTrue('from middleware' in str(from_md),
                        'unexpected value ({0}) of cookie that set via middleware'.format(from_md))

    def test_reraise_in_mmiddleware(self):
        """
        horns_hooves.middleware.ProcessException "reraices"  404 to 500
        """
        res = self.client.get('/qwerty_does_not_exists_page/')
        self.assertEqual(res.status_code, 500)
