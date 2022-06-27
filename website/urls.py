from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("observation/", views.listObservation.as_view(), name="observation"),
    path(
        "observation/<int:pk>",
        views.viewObservation.as_view(),
        name="observation-detail",
    ),
    path("recherche/", views.search, name="search"),
]
