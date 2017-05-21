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

# 사실 이런식으로 나눠줘야 합니다.
# 그때 그때 어플리케이션, 토큰을 받아오는 것은 비효율적입니다.
# 우리는 개발자 이기 때문에, 게을러요
# 이렇게 사용하는게 더 테스트의 생산성이 더 높습니다.

pytestmark = pytest.mark.django_db
Application = get_application_model()


class TestPostsBase(APITestCase, TestCaseUtils):

    def setUp(self):

        # 이런식으로 천천히 확장해가면 쉽게 테스트를 관리? 할수
        # 있습니다.
        self.admin_user = mixer.blend(
                'auth.User',
                username='superBadass',
                is_staff=True,
                is_superuser=True)

    def tearDown(self):
        pass

    def set_oauth2_application_by_admin(self):
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        application = Application.objects.create(
           name="TEST_PINTECH_APPLICATION",
           user=super_user,
           client_type=Application.CLIENT_PUBLIC,
           authorization_grant_type=Application.GRANT_PASSWORD,
        )
        return application

    def get_token(self, access_user, app):
        access_token = AccessToken.objects.create(
            user=access_user,
            scope='read write',
            expires=timezone.now() + timedelta(seconds=300),
            token=f'{get_random_string(length=64)}-----{access_user.username}',
            application=app
        )
        return access_token.token
