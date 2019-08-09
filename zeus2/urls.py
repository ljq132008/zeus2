"""zeus2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from .swagger import get_swagger_view

api_v1 = [
   path('users/v1/', include('users.urls.api_urls', namespace='api-users')),
   path('assets/v1/', include('assets.urls.api_urls', namespace='api-assets')),
   path('perms/v1/', include('perms.urls.api_urls', namespace='api-perms')),
   # path('terminal/v1/', include('terminal.urls.api_urls', namespace='api-terminal')),
   path('ops/v1/', include('ops.urls.api_urls', namespace='api-ops')),
   # path('audits/v1/', include('audits.urls.api_urls', namespace='api-audits')),
   path('orgs/v1/', include('orgs.urls.api_urls', namespace='api-orgs')),
   path('settings/v1/', include('settings.urls.api_urls', namespace='api-settings')),
   path('authentication/v1/', include('authentication.urls.api_urls', namespace='api-auth')),
]

api_v2 = [
   # path('terminal/v2/', include('terminal.urls.api_urls_v2', namespace='api-terminal-v2')),
   # path('users/v2/', include('users.urls.api_urls_v2', namespace='api-users-v2')),
]

api_v1_patterns = [
    path('api/', include(api_v1))
]

api_v2_patterns = [
    path('api/', include(api_v2))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(api_v1_patterns)),
]

if settings.DEBUG:
    urlpatterns += [
        re_path('^swagger(?P<format>\.json|\.yaml)$',
                get_swagger_view().without_ui(cache_timeout=1), name='schema-json'),
        path('docs/', get_swagger_view().with_ui('swagger', cache_timeout=1), name="docs"),
        path('redoc/', get_swagger_view().with_ui('redoc', cache_timeout=1), name='redoc'),

        re_path('^v2/swagger(?P<format>\.json|\.yaml)$',
                get_swagger_view().without_ui(cache_timeout=1), name='schema-json'),
        path('docs/v2/', get_swagger_view("v2").with_ui('swagger', cache_timeout=1), name="docs"),
        path('redoc/v2/', get_swagger_view("v2").with_ui('redoc', cache_timeout=1), name='redoc'),
    ]