# coding: utf8
""" 
@File: urls.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/16 21:42
"""

import os, sys

from django.urls.conf import re_path
from users import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(route=r'^users/$', view=csrf_exempt(views.UsersView.as_view()), name='users'),
    re_path(route=r'^user/(?P<uid>\d+)/$', view=csrf_exempt(views.UserView.as_view()), name='user'),
]
