from django.contrib import admin

# Register your models here.
from .models import *

# Modèles de base
admin.site.register(TypeObservation)
admin.site.register(LieuObservation)
admin.site.register(LieuStockage)
admin.site.register(Batiment)
admin.site.register(Instrument)
admin.site.register(Caracteristique)
admin.site.register(TypeEvenement)

#
# Supports
#

# Formulaire tableau pour les images
class ImageSupportInline(admin.TabularInline):
    model = ImageSupport
    extra = 2  # how many rows to show


class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 2


class SupportAdmin(admin.ModelAdmin):
    inlines = (ImageSupportInline, ObservationInline)
    list_display = (
        "__str__",
        "instrument",
        "lieuobservation",
        "lieustockage",
        "type",
        "numero",
    )


admin.site.register(Support, SupportAdmin)

#
# Observations
#

# Formulaire tableau pour les images
class ImageObservationInline(admin.TabularInline):
    model = ImageObservation
    extra = 2  # how many rows to show


class EvenementInline(admin.TabularInline):
    model = Evenement
    extra = 2


class ObservationAdmin(admin.ModelAdmin):
    inlines = (ImageObservationInline, EvenementInline)
    list_display = (
        "__str__",
        "support",
        "typeobservation",
        "date",
    )


admin.site.register(Observation, ObservationAdmin)

#
# Evenements
#

# Formulaire tableau pour les caractéristiques
class CaracteristiqueEvenementInLine(admin.TabularInline):
    model = CaracteristiqueEvenement
    extra = 2


# Formulaire tableau pour les images
class ImageEvenementInline(admin.TabularInline):
    model = ImageEvenement
    extra = 2  # how many rows to show


class EvenementAdmin(admin.ModelAdmin):
    inlines = (
        CaracteristiqueEvenementInLine,
        ImageEvenementInline,
    )
    list_display = (
        "__str__",
        "observation",
        "support",
        "type_evenement",
        "date",
    )


admin.site.register(Evenement, EvenementAdmin)

#
# Collections
#
class CollectionObservationInline(admin.TabularInline):
    model = CollectionObservation
    extra = 2  # how many rows to show


class CollectionAdmin(admin.ModelAdmin):
    inlines = (CollectionObservationInline,)
    list_display = (
        "__str__",
        "nom",
    )


admin.site.register(Collection, CollectionAdmin)
