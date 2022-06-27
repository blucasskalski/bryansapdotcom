from django.shortcuts import render
from django import http
from django.views import generic
from django.db import models
from django import forms

import django_filters

from .forms import ObservationForm
from .models import Support, Observation, Evenement, TypeEvenement, Caracteristique


# Create your views here.


def index(request):
    # return HttpResponse("Web Server is ON, this is a placeholder.")
    num_support = Support.objects.all().count()
    num_observation = Observation.objects.all().count()
    num_evenement = Evenement.objects.all().count()
    num_typeevenement = TypeEvenement.objects.all().count()

    context = {
        "num_support": num_support,
        "num_observation": num_observation,
        "num_evenement": num_evenement,
        "num_typeevenement": num_typeevenement,
    }

    return render(request, "shInvSol/view.html", context=context)


def addObservation(request, support_id):
    support = Support.objects.get(id_support=support_id)
    form = ObservationForm()
    context = {"form": form}
    print("-------------------------")
    print("ForeignKey support_id :")
    print(support_id)
    print("Support lié à l'ID : ")
    print(support)
    print("-------------------------")
    if request.method == "GET":
        return render(request, "shInvSol/addObservation.html", context)
    elif request.method == "POST":
        form = ObservationForm(request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect("/InvSol/addEvenement", context)


class listSupport(generic.ListView):
    model = Support
    paginate_by = 5


class viewSupport(generic.DetailView):
    model = Support


class listObservation(generic.ListView):
    model = Observation
    paginate_by = 5


class viewObservation(generic.DetailView):
    model = Observation


class listEvenement(generic.ListView):
    model = Evenement
    paginate_by = 5


class viewEvenement(generic.DetailView):
    model = Evenement


class ObservationFilter(django_filters.FilterSet):
    observation__date_debut = django_filters.DateFilter(
        field_name="date", lookup_expr="gte"
    )
    observation__date_fin = django_filters.DateFilter(
        field_name="date", lookup_expr="lte"
    )

    class Meta:
        model = Observation
        fields = ["support", "typeobservation", "interet", "date"]


class EvenementFilter(django_filters.FilterSet):
    caracteristiques = django_filters.ModelMultipleChoiceFilter(
        queryset=Caracteristique.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    observation__date_debut = django_filters.DateFilter(
        field_name="observation__date", lookup_expr="gte"
    )
    observation__date_fin = django_filters.DateFilter(
        field_name="observation__date", lookup_expr="lte"
    )

    class Meta:
        model = Evenement
        fields = [
            "type_evenement",
            "caracteristiques",
            "latitude",
            "longitude",
            "importance",
            "brillance",
            "aire_mesuree",
            "aire_corrigee",
            "interet",
            "support",
            "observation__typeobservation",
            "observation__interet",
            "observation__date",
            "support__type",
            "support__instrument",
            "support__lieustockage",
            "support__lieuobservation",
            "support__numero",
            "support__diametre_solaire",
            "support__manquant",
            "support__abime",
            "support__interet",
        ]


def search(request):

    # si on ne renseigne pas la date de fin, on la met = date de debut
    if (
        "observation__date_fin" in request.POST
        and "observation__date_debut" in request.POST
        and request.POST["observation__date_fin"] == ""
        and request.POST["observation__date_debut"] != ""
    ):
        request.POST._mutable = True
        request.POST["observation__date_fin"] = request.POST["observation__date_debut"]
        request.POST._mutable = False

    # Il faut aussi pouvoir retrouver les observations sans événement
    observation_list_search = Observation.objects.all()
    obs_filter = ObservationFilter(request.POST, queryset=observation_list_search)

    evenement_list_search = Evenement.objects.all()
    evn_filter = EvenementFilter(
        request.POST,
        queryset=evenement_list_search,
    )

    supports = []
    observations = []

    for evn in evn_filter.qs:
        if evn.support not in supports:
            supports.append(evn.support)
        if evn.observation not in observations:
            observations.append(evn.observation)

    for obs in obs_filter.qs:
        if obs.support not in supports:
            supports.append(obs.support)
        if obs not in observations:
            observations.append(obs)

    return render(
        request,
        "shInvSol/evenement_list_search.html",
        {"filter": evn_filter, "supports": supports, "observations": observations},
    )
