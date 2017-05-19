#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from posts.models import ExtendUser


class ExtendUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendUser
        fields = ('user', 'mobile')
