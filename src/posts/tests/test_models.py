#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from datetime import timedelta

import pytest
from mixer.backend.django import mixer

from oauth2_provider.models import get_application_model, AccessToken

from .base import TestPostsBase

pytestmark = pytest.mark.django_db

Application = get_application_model()


class TestPostModel(TestPostsBase):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_users_with_mixer(self):
        # 좋은 방법은 아닙니다.
        for cnt in range(100):
            obj = mixer.blend('auth.User', is_staff=True)
            print(obj.username)

        assert User.objects.count() == 100, 'Should be equal!!'

    def test_send_get_request_to_user_lists(self):
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        application = Application.objects.create(
           name="TEST_PINTECH_APPLICATION",
           user=super_user,
           client_type=Application.CLIENT_PUBLIC,
           authorization_grant_type=Application.GRANT_PASSWORD,
        )
        assert Application.objects.count() == 1, 'Should be equal'

        access_user = mixer.blend('auth.User', username='Daniel')
        # access_user = User.objects.get(username='')
        access_token = AccessToken.objects.create(
            user=access_user,
            scope='read write',
            expires=timezone.now() + timedelta(seconds=300),
            # get_random_string(length=32)
            # magic of f-string
            token=f'{get_random_string(length=64)}-----{access_user.username}',
            application=application
        )
        print(access_token.token)
        assert access_token is not None, 'Should not none'

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {0}'.format(access_token.token)
        )
        url = reverse('user-list')
        print(url)
        response = self.client.get(url, format='json')
        print(response.content)
        assert response.status_code == 200, f"{response.content}"

    @pytest.mark.skip(reason="skip it for a moment")
    def test_oauth2_is_work_or_not(self):
        # 임시로 슈퍼유져를 만듭니다.
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        # Ouath2 에다가 APP을 등록합니다.
        Application.objects.create(
           name="TEST_PINTECH_APPLICATION",
           user=super_user,
           client_type=Application.CLIENT_PUBLIC,
           authorization_grant_type=Application.GRANT_PASSWORD,
        )
        assert Application.objects.count() == 1, 'Should be equal'
        # 아직도 잘 모르겠다..
        # 당연하죠 이런식으로 쓰라고 했으니까요.
        # 앱을 생성했으니 이제 유져를 등록해서 토큰을 받아올까요?

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_oauth2_token(self):
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        application = Application.objects.create(
           name="TEST_PINTECH_APPLICATION",
           user=super_user,
           client_type=Application.CLIENT_PUBLIC,
           authorization_grant_type=Application.GRANT_PASSWORD,
        )
        assert Application.objects.count() == 1, 'Should be equal'

        access_user = mixer.blend('auth.User', username='Daniel')
        # access_user = User.objects.get(username='')
        access_token = AccessToken.objects.create(
            user=access_user,
            scope='read write',
            expires=timezone.now() + timedelta(seconds=300),
            token=f'{get_random_string(length=64)}-----{access_user.username}',
            application=application
        )
        print(access_token.token)
        assert access_token is not None, 'Should not be NoneType'
