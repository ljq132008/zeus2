# coding:utf-8
#

from __future__ import absolute_import

from django.urls import path
from .auth import *

app_name = 'authentication'


urlpatterns = [
    # path('token/', UserToken.as_view(), name='user-token'),
    path('auth/', UserAuthApi.as_view(), name='user-auth'),
    path('connection-token/', UserConnectionTokenApi.as_view(), name='connection-token'),
    path('otp/auth/', UserOtpAuthApi.as_view(), name='user-otp-auth'),
]

