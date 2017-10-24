# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from page.models import Category, Good
from api.serializers import GoodSerializer


ROOT_ID = 1


class ApiAuthTestCase(APITestCase):
    fixtures = ['api_test_data.json']

    def test_generate_token_for_new_user(self):
        """
        for check action api.models.create_auth_token (post_save User)
        """
        _user = User.objects.create_user('tusr', 'tust@sr.com', '!1q2w3e4R')
        Token.objects.get(user=_user)

    def test_obtain_auth_token(self):
        token_obtain_url = reverse('obtain_auth_token')
        res = self.client.post(token_obtain_url, {"username": "usert", "password": "!1q2w3e4R"}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in res.data.keys())

    def test_invalid_token(self):
        cats_url = reverse('categories_list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'not_exists_token')
        res = self.client.get(cats_url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_token(self):
        cats_url = reverse('categories_list')
        token = Token.objects.get(user__username='usert')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.get(cats_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_restrict_changes_from_ro_user(self):
        cats_add_url = reverse('category_add')
        token = Token.objects.get(user__username='usert')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.post(cats_add_url, {'name': 'test_restrict_ro', 'description': '.'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class ApiCategoriesTestCase(APITestCase):
    # TODO: add tests for CategorySerializer
    fixtures = ['api_test_data.json']

    @classmethod
    def setUpTestData(cls):
        token = Token.objects.get(user__username='root')
        cls.key = token.key
        cls.cat = Category.objects.create(name='from_api_tests', description='xxxxxxxxxxxx')

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.key)

    def test_categories_list(self):
        list_url = reverse('categories_list')
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data))

    def test_categories_detail(self):
        detail_url = reverse('category_detail', kwargs={'pk': self.cat.id})
        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        excp_cat = {'name': self.cat.name, 'description': self.cat.description, 'id': self.cat.id, 'changed_by': None}
        self.assertEqual(res.data, excp_cat)

    def test_categories_add(self):
        add_url = reverse('category_add')
        new_cat = {'name': 'name_new_cat', 'description': 'test_api'}
        add_res = self.client.post(add_url, new_cat, format='json')
        self.assertEqual(add_res.status_code, status.HTTP_201_CREATED)

        new_cat['id'] = add_res.data['id']
        new_cat['changed_by'] = ROOT_ID
        detail_url = reverse('category_detail', kwargs={'pk': new_cat['id']})
        new_cat_res = self.client.get(detail_url)
        self.assertEqual(new_cat_res.data, new_cat)

    def test_categories_del(self):
        cat_id = self.cat.id
        del_url = reverse('category_del', kwargs={'pk': cat_id})
        del_res = self.client.post(del_url, format='json')
        self.assertEqual(del_res.status_code, status.HTTP_204_NO_CONTENT)

        detail_url = reverse('category_detail', kwargs={'pk': cat_id})
        detail_res = self.client.get(detail_url)
        self.assertEqual(detail_res.status_code, status.HTTP_404_NOT_FOUND)

    def test_categories_update(self):
        upd_url = reverse('category_update', kwargs={'pk': self.cat.id})
        new_desc = 'test update'
        upd_res = self.client.post(upd_url, {'description': new_desc}, format='json')
        self.assertEqual(upd_res.status_code, status.HTTP_200_OK)

        detail_url = reverse('category_detail', kwargs={'pk': self.cat.id})
        detail_res = self.client.get(detail_url)
        excp_cat = {'id': self.cat.id, 'name': self.cat.name, 'description': new_desc, 'changed_by': ROOT_ID}
        self.assertEqual(detail_res.data, excp_cat)


class ApiGoodsTestCase(APITestCase):
    # TODO: add tests or GoodSerializer
    fixtures = ['api_test_data.json']

    @classmethod
    def setUpTestData(cls):
        token = Token.objects.get(user__username='root')
        cls.key = token.key
        cls.cat = Category.objects.create(name='from_api_tests', description='.')
        cls.good = Good.objects.create(name='good_from_api_tests', category=cls.cat)

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.key)

    def test_goods_list(self):
        list_url = reverse('good_list')
        res = self.client.get(list_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data))

    def test_goods_detail(self):
        detail_url = reverse('good_detail', kwargs={'pk': self.good.id})
        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        exp_good = dict((i.name, i.value) for i in GoodSerializer(self.good))
        self.assertEqual(res.data, exp_good)

    def test_goods_add(self):
        add_url = reverse('good_add')
        new_good = {'name': 'from_test_good_add', 'category': self.cat.id, 'changed_by': ROOT_ID}
        res = self.client.post(add_url, new_good, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        new_good['id'] = res.data['id']
        detail_url = reverse('good_detail', kwargs={'pk': new_good['id']})
        new_good_res = self.client.get(detail_url)
        self.assertTrue(all(new_good_res.data[k] == v for k, v in new_good.items()))

    def test_goods_del(self):
        good_id = self.good.id
        del_url = reverse('good_del', kwargs={'pk': good_id})
        res = self.client.post(del_url, format='json')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        detail_url = reverse('good_detail', kwargs={'pk': good_id})
        res_detail = self.client.get(detail_url)
        self.assertEqual(res_detail.status_code, status.HTTP_404_NOT_FOUND)

    def test_goods_update(self):
        update_url = reverse('good_update', kwargs={'pk': self.good.id})
        new_desc = 'test update'
        exp_good = dict((i.name, i.value) for i in GoodSerializer(self.good))
        exp_good['description'] = new_desc
        exp_good['changed_by'] = ROOT_ID
        res = self.client.post(update_url, {'description': new_desc}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        detail_url = reverse('good_detail', kwargs={'pk': self.good.id})
        detail_res = self.client.get(detail_url)
        self.assertEqual(detail_res.data, exp_good)
