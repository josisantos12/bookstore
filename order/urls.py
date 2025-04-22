#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


from order import viewsets
from django.urls import path
from .views import GerarTokenAPIView

router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")


urlpatterns = [
    path("", include(router.urls)),

    path('api-token-auth/', obtain_auth_token),

    path('api/token/', GerarTokenAPIView.as_view(), name='gerar_token'),

]
