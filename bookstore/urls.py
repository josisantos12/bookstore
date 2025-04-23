from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
import debug_toolbar
from bookstore import views
from .views import MeuModeloViewSet  # Importe aqui o seu ViewSet

router = DefaultRouter()
router.register(r'meumodelo', MeuModeloViewSet)  # Registro do MeuModeloViewSet

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("update_server/", views.update, name="update"),
    path('hello/', views.hello_world, name='hello_world'),
    path("", include(router.urls)),  # Inclua o roteador principal
]