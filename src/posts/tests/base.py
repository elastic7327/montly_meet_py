#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 사실 이런식으로 나눠줘야 합니다.
# 그때 그때 어플리케이션, 토큰을 받아오는 것은 비효율적입니다.
# 우리는 개발자 이기 때문에, 게을러요
# 이렇게 사용하는게 더 테스트의 생산성이 더 높습니다.


class TestPostModelBase(object):

    def setUp(self):
        self.admin_token = "?"

    def tearDown(self):
        pass

    def create_token(self, username, password):
        assert 1 is not 2
