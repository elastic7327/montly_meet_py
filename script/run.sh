#!/bin/sh

cd ../src && python3 manage.py runserver --settings=bookclub.settings.development
# 이런식으로 못찾을때는.. 그냥 플러그인의 힘을 빌리자
# cd ../src && python3 manage.py show_urls --settings=bookclub.settings.development
