from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "addObservation/<int:support_id>/", views.addObservation, name="addObservation"
    ),
    path("support/", views.listSupport.as_view(), name="support"),
    path("support/<int:pk>", views.viewSupport.as_view(), name="support-detail"),
    path("observation/", views.listObservation.as_view(), name="observation"),
    path(
        "observation/<int:pk>",
        views.viewObservation.as_view(),
        name="observation-detail",
    ),
    path("evenement/", views.listEvenement.as_view(), name="Evenement"),
    path("evenement/<int:pk>", views.viewEvenement.as_view(), name="Evenement-detail"),
    path("recherche/", views.search, name="search"),
]
