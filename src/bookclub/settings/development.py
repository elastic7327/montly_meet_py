#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 이제는 인메모리로!!
        'NAME': ':memory:',
    }
}
