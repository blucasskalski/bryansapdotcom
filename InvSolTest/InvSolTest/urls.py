"""InvSolTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import static
from filebrowser.sites import site
from pathlib import Path

urlpatterns = [
    path("admin/filebrowser/", site.urls),
    path("admin/", admin.site.urls),
    path("InvSol/", include("shInvSol.urls")),
    path(
        "media/uploads/<path:path>",
        static.serve,
        kwargs={
            "document_root": Path(settings.MEDIA_ROOT, settings.FILEBROWSER_DIRECTORY)
        },
    ),
    path(
        "media/_versions/<path:path>",
        static.serve,
        kwargs={
            "document_root": Path(
                settings.MEDIA_ROOT, settings.FILEBROWSER_VERSIONS_BASEDIR
            )
        },
    ),
]
