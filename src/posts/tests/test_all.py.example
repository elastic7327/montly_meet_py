#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from datetime import timedelta

from rest_framework import status
from rest_framework.test import APITestCase

import pytest
from mixer.backend.django import mixer

from oauth2_provider.models import get_application_model, AccessToken
from oauth2_provider.tests.test_utils import TestCaseUtils

pytestmark = pytest.mark.django_db

Application = get_application_model()


class TestPostModel(APITestCase, TestCaseUtils):

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
    def test_send_post_request_to_user_lists(self):
        url = reverse('user-list')
        for index in range(10):
            data = {
                    'username': 'Daniel_Kim{}'.format(index),
                    'password': 'DIBIUP IPO GOGOGO',
                    'email': 'elastic7327@gmail.com',
                    'is_active': True
            }
            print(url)
            response = self.client.post(url, data=data, format='json')
            print(response.content)
            assert response.status_code == status.HTTP_201_CREATED, f"{response.content}"

        assert User.objects.count() == 10, 'Should be equal'

        url = reverse('user-list')
        print(url)
        response = self.client.get(url, data=data, format='json')
        print(response.content)
        assert response.status_code == status.HTTP_200_OK, f"{response.content}"

        url = reverse('user-detail', args=[1])
        print(url)
        response = self.client.get(url, format='json')
        print(response.content)
        assert response.status_code == status.HTTP_200_OK, f"{response.content}"

        url = reverse('user-detail', args=[1])
        data = {
                'username': 'AWESOME_DIBIUP_TEAMS',
                'password': 'DIBIUP IPO GOGOGO',
                'email': 'dibiup@gmail.com',
                'is_active': False
        }
        print(url)

        # PYTHON 3.6.1 부터 조금 이상해짐 쓸대없이.. 덤프해서 넘기고 그래야함.
        # 유져 pk 값이 1인 대상의 자료값을 바꿔준다.
        response = self.client.patch(
                url,
                data=json.dumps(data),
                content_type='application/json'
        )
        print(response.content)
        assert response.status_code == status.HTTP_200_OK, f"{response.content}"

        # 변경 사항을 체크 할 수 있음.
        # 뭔가 좀 변한거 같지 않나요?
        # 리턴값을 확인 해보세요
        url = reverse('user-detail', args=[1])
        print(url)
        response = self.client.get(url, format='json')
        print(response.content)
        assert response.status_code == status.HTTP_200_OK, f"{response.content}"

        # 그럼 한번 지워볼까요?
        url = reverse('user-detail', args=[1])
        print(url)
        response = self.client.delete(url, format='json')
        print(response.content)
        assert response.status_code == status.HTTP_204_NO_CONTENT, f"{response.content}"

        # 확실하게 날려버렸나 다시 한번 확인해 볼까요?
        url = reverse('user-detail', args=[1])
        print(url)
        response = self.client.get(url, format='json')
        print(response.content)
        # Booom!  성공!
        assert response.status_code == status.HTTP_404_NOT_FOUND, f"{response.content}"

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
