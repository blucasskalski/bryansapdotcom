"""
Fichier de déclaration des modèles pour la base de donnée InvSol.
Prototype du 23/05/2022
"""

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from filebrowser.fields import FileBrowseField


class Observation(TimeStampedModel):
    # Relation Observation - Support
    support = models.ForeignKey("Support", on_delete=models.CASCADE, related_name="observations")

    # Relation Observation - TypeObservation
    typeobservation = models.ForeignKey(
        "TypeObservation", on_delete=models.CASCADE, default=None
    )
    id_observation = models.AutoField(primary_key=True)
    date = models.DateField()
    heure_debut = models.TimeField(null=True, blank=True)
    heure_fin = models.TimeField(null=True, blank=True)
    interet = models.BooleanField(null=True, blank=True)
    remarques = models.TextField(null=True, blank=True)

    def __str__(self):
        str_hd = f" {self.heure_debut} " if self.heure_debut else ""
        str_hf = f"- {self.heure_fin} " if self.heure_fin else ""
        str_h = f"({str_hd}{str_hf})" if str_hd else ""
        a = f"{self.date} {str_h} [{self.typeobservation}]"
        return a

    pass


class Evenement(TimeStampedModel):
    # Relation Evenement - Observation
    observation = models.ForeignKey(
        Observation, on_delete=models.CASCADE, related_name="evenements"
    )

    # Relation Evenement - Support
    support = models.ForeignKey("Support", on_delete=models.CASCADE)

    # Relation Evenement - TypeEvenement
    type_evenement = models.ForeignKey(
        "TypeEvenement", on_delete=models.CASCADE, default=None
    )

    caracteristiques = models.ManyToManyField(
        "Caracteristique",
        related_name="evenements",
        through="CaracteristiqueEvenement",
    )

    BrillanceEruption = Choices(
        ("F", _("Faible")),
        ("N", _("Normale")),
        ("B", _("Brillante")),
    )

    ImportanceEruption = Choices(
        ("S", _("S")),
        ("1-", _("1-")),
        ("1", _("1")),
        ("1+", _("1+")),
        ("2", _("2")),
        ("3", _("3")),
        ("4", _("4")),
    )

    id_evenement = models.AutoField(primary_key=True)
    date = models.DateField()
    numero = models.CharField(max_length=255, null=True, blank=True)
    heure_debut = models.TimeField(null=True, blank=True)
    heure_fin = models.TimeField(null=True, blank=True)
    heure_max_intensite = models.TimeField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    importance = models.CharField(
        max_length=2, choices=ImportanceEruption, null=True, blank=True
    )
    brillance = models.CharField(
        max_length=1, choices=BrillanceEruption, null=True, blank=True
    )
    heure_releve_aire = models.TimeField(null=True, blank=True)
    aire_mesuree = models.FloatField(null=True, blank=True)
    aire_corrigee = models.FloatField(null=True, blank=True)
    remarques = models.TextField(null=True, blank=True)
    interet = models.BooleanField(null=True, blank=True)
    strdate = str(date)

    def __str__(self):
        str_numero = f"N° {self.numero} | " if self.numero else ""
        return f"{str_numero}{self.type_evenement} du {self.observation}"

    pass


class Support(TimeStampedModel):
    # Relation Support- Instrument
    instrument = models.ForeignKey("Instrument", on_delete=models.CASCADE, default=None)

    # Relation Support - LieuObservation
    lieuobservation = models.ForeignKey("LieuObservation", on_delete=models.CASCADE)

    # Relation Support - LieuStockage
    lieustockage = models.ForeignKey("LieuStockage", on_delete=models.CASCADE)

    TypeSupport = Choices(
        ("Film"),
        ("Plan Film"),
        ("CDrom"),
        ("DVD"),
        ("Plaque"),
        ("Papier"),
    )

    id_support = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, choices=TypeSupport)
    numero = models.CharField(max_length=255)
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    diametre_solaire = models.FloatField(null=True, blank=True)
    remarques = models.TextField(null=True, blank=True)
    manquant = models.BooleanField(null=True, blank=True)
    abime = models.BooleanField(null=True, blank=True)
    interet = models.BooleanField(null=True, blank=True)

    def __str__(self):
        str_titre = f"({self.titre})" if self.titre else ""
        str_date = (
            f"{self.date_debut} au {self.date_fin}"
            if self.date_fin
            else f"{self.date_debut}"
        )
        a = f"{str_titre} {self.type} n° {self.numero} du {str_date}"
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


class LieuStockage(TimeStampedModel):
    # Relation LieuStockage-Batiment
    batiment = models.ForeignKey("Batiment", on_delete=models.CASCADE)
    id_lieu_stockage = models.AutoField(primary_key=True)
    piece = models.CharField(max_length=255)
    emplacement = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        str_emplacement = f"({self.emplacement})" if self.emplacement else ""
        a = f"Batiment {str(self.batiment)} piece {self.piece} {str_emplacement}"
        return a

    pass


class Batiment(TimeStampedModel):
    id_batiment = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

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


#  class Image(TimeStampedModel):
#      id_image = models.AutoField(primary_key=True)
#      fichier = FileBrowseField("Image", max_length=200, directory="", extensions=[".jpg", ".png"], blank=True)
#      description = models.TextField(null=True, blank=True)
#      pass


class ImageEvenement(TimeStampedModel):
    # Relation ImageEvenement - Evenement
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    image = FileBrowseField(
        "Image", max_length=200, directory="", extensions=[".jpg", ".png"], blank=True
    )
    description = models.TextField(null=True, blank=True)
    id = models.AutoField(primary_key=True)
    pass


class ImageObservation(TimeStampedModel):
    # Relation ImageObservation - Observation
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE, default=None)

    # Relation ImageObservation - Image
    image = FileBrowseField(
        "Image", max_length=200, directory="", extensions=[".jpg", ".png"], blank=True
    )
    description = models.TextField(null=True, blank=True)
    id = models.AutoField(primary_key=True)
    pass


class ImageSupport(TimeStampedModel):
    # Relation ImageSupport - Support
    support = models.ForeignKey(
        Support, on_delete=models.CASCADE, default=None, related_name="img_s"
    )

    # Relation ImageSupport - Image
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
    ordre = models.IntegerField()

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


class CaracteristiqueEvenement(TimeStampedModel):
    # Relation CaracteristiqueEvenement - Evenement
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    # Relation CaracteristiqueEvenement - Caracteristique
    caracteristique = models.ForeignKey("Caracteristique", on_delete=models.CASCADE)

    id_caracteristiqueevenement = models.AutoField(primary_key=True)
    # id_evenement = models.IntegerField()
    pass


class Caracteristique(TimeStampedModel):
    id_caracteristique = models.AutoField(primary_key=True)
    caracteristique = models.CharField(max_length=255)

    def __str__(self):
        return self.caracteristique

    pass


class TypeEvenement(TimeStampedModel):
    id_typeevenement = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    abreviation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nom

    pass
