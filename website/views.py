from django.shortcuts import render
from django import http
from django.views import generic
from django.db import models
from django import forms

import django_filters

from .forms import ObservationForm
from .models import Observation


# Create your views here.


def index(request):
    # return HttpResponse("Web Server is ON, this is a placeholder.")
    num_observation = Observation.objects.all().count()

    latest = Observation.objects.order_by('-date')
    context = {
        "num_observation": num_observation,
        "latest": latest,
    }

    return render(request, "website/view.html", context=context)

class listObservation(generic.ListView):
    model = Observation
    paginate_by = 5


class viewObservation(generic.DetailView):
    model = Observation

class ObservationFilter(django_filters.FilterSet):
    class Meta:
        model = Observation
        fields = ["typeobservation", "temps_exp", "date"]


def search(request):

    # Il faut aussi pouvoir retrouver les observations sans événement
    observation_list_search = Observation.objects.all()
    obs_filter = ObservationFilter(
        request.POST, 
        queryset=observation_list_search,
    )

    observations = []

    for obs in obs_filter.qs:
        if obs not in observations:
            observations.append(obs)

    return render(
        request,
        "website/full_list_search.html",
        {"observations": observations, "filter": obs_filter},
    )
