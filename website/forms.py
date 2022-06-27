from django.forms import ModelForm
from .models import *
from django import forms


class ObservationForm(ModelForm):
    class Meta:
        model = Observation
        fields = "__all__"


class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = "__all__"


class LieuObservationForm(ModelForm):
    class Meta:
        model = LieuObservation
        fields = "__all__"


class TypeObservationForm(ModelForm):
    class Meta:
        model = TypeObservation
        fields = "__all__"


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"


class ImageObservationForm(ModelForm):
    class Meta:
        model = ImageObservation
        fields = "__all__"