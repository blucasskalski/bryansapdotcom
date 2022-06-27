"""
Fichier de déclaration des modèles pour la base de donnée pour website.
Prototype du 27/06/2022
"""

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from filebrowser.fields import FileBrowseField


class Observation(TimeStampedModel):
    # Relation Observation - TypeObservation
    typeobservation = models.ForeignKey(
        "TypeObservation", on_delete=models.CASCADE, default=None
    )
    id_observation = models.AutoField(primary_key=True)
    nom_obj = models.TextField(default="Undefined")
    temps_exp = models.IntegerField(default=0)
    nb_exp = models.IntegerField(default=1)
    date = models.DateField(null=True, blank=True)
    remarques = models.TextField(null=True, blank=True)

    def __str__(self):
        str_dt = f" {self.date} " if self.date else ""
        a = f"{self.nom_obj} | {self.typeobservation} [{str_dt}]"
        return a

    pass


class Instrument(TimeStampedModel):
    id_instrument = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

    pass


class LieuObservation(TimeStampedModel):
    id_lieu_observation = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    IAU_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nom

    pass

class TypeObservation(TimeStampedModel):
    id_type_observation = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    lg_onde = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nom

    pass


class ImageObservation(TimeStampedModel):
    # Relation ImageObservation - Observation
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE, default=None, related_name="img_o")

    # Relation ImageObservation - Image
    image = FileBrowseField(
        "Image", max_length=200, directory="", extensions=[".jpg", ".png"], blank=True
    )
    description = models.TextField(null=True, blank=True)
    id = models.AutoField(primary_key=True)
    pass

class CollectionObservation(TimeStampedModel):
    collection = models.ForeignKey(
        "Collection", on_delete=models.CASCADE, related_name="+", default=None
    )
    observation = models.ForeignKey(
        "Observation", on_delete=models.CASCADE, related_name="+", default=None
    )

    id_collectionobservation = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.ordre)

    pass


class Collection(TimeStampedModel):
    id_collection = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    observations = models.ManyToManyField(
        Observation,
        related_name="collections",
        through="CollectionObservation",
    )

    def __str__(self):
        return self.nom

    pass
