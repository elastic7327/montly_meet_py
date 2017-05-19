#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from rest_framework import viewsets

from posts.models import ExtendUser
from posts.serializers import ExtendUserSerializer


class ExtendUserViewSet(viewsets.ModelViewSet):
    serializer_class = ExtendUserSerializer
    queryset = ExtendUser.objects.all()
