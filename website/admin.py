from django.contrib import admin

# Register your models here.
from .models import *

# Modèles de base
admin.site.register(TypeObservation)
admin.site.register(LieuObservation)
admin.site.register(Instrument)


#
# Supports
#


class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 2


#
# Observations
#

# Formulaire tableau pour les images
class ImageObservationInline(admin.TabularInline):
    model = ImageObservation
    extra = 2  # how many rows to show


class ObservationAdmin(admin.ModelAdmin):
    inlines = (ImageObservationInline,)
    list_display = (
        "__str__",
        "typeobservation",
        "date",
    )


admin.site.register(Observation, ObservationAdmin)


#
# Collections
#
class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 2  # how many rows to show

admin.site.register(Collection)
