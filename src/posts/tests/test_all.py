#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from posts.models import ExtendUser

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


# Create your tests here.
class TestPostModel(TestCase):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_users_and_exuser(self):
        user_obj = User.objects.create(
            username="Hello User!",
            is_staff=False,
            is_superuser=False)
        assert User.objects.count() == 1, 'Should be equal!'

        ExtendUser.objects.create(user=user_obj, mobile='010203012')
        assert ExtendUser.objects.count() == 1, 'Should be equal!'

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_users_and_exuser_with_mixer(self):

        # 좋은 방법은 아닙니다.
        for cnt in range(100):
            obj = mixer.blend('auth.User', is_staff=True)
            print(obj.username)

        assert User.objects.count() == 100, 'Should be equal!!'

        for cnt in range(100):
            obj = mixer.blend('posts.ExtendUser')
            print(obj.mobile)

        assert ExtendUser.objects.count() == 100, 'Should be equal!!'

    def test_extenduser_list_view_send_get_request(self):
        url = reverse('extenduser-list')
        print (url)
        response = self.client.get(url, format='json')
        print (response.content)
        assert response.status_code == 200, f'{response.content}'
