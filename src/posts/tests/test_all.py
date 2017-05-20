#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from posts.models import ExtendUser
from rest_framework import status

import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


# Create your tests here.
class TestPostModel(TestCase):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_create_users_with_mixer(self):
        # 좋은 방법은 아닙니다.
        for cnt in range(100):
            obj = mixer.blend('auth.User', is_staff=True)
            print(obj.username)

        assert User.objects.count() == 100, 'Should be equal!!'

    def test_send_get_request_to_user_lists(self):
        url = reverse('user-list')
        print (url)
        response = self.client.get(url, format='json')
        print (response.content)

        assert response.status_code == 200, f"{response.content}"

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
