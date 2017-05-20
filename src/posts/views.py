#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import viewsets

from posts.models import ExtendUser
from posts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
