from django.forms import ModelForm
from .models import *
from django import forms


class ObservationForm(ModelForm):
    class Meta:
        model = Observation
        fields = "__all__"


class EvenementForm(ModelForm):
    caracteristiques = forms.ModelMultipleChoiceField(
        queryset=Caracteristique.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Evenement
        fields = "__all__"


class SupportForm(ModelForm):
    class Meta:
        model = Support
        fields = "__all__"


class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = "__all__"


class LieuObservationForm(ModelForm):
    class Meta:
        model = LieuObservation
        fields = "__all__"


class LieuStockageForm(ModelForm):
    class Meta:
        model = LieuStockage
        fields = "__all__"


class BatimentForm(ModelForm):
    class Meta:
        model = Batiment
        fields = "__all__"


# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = '__all__'


class ImageSupportForm(ModelForm):
    class Meta:
        model = ImageSupport
        fields = "__all__"


class TypeObservationForm(ModelForm):
    class Meta:
        model = TypeObservation
        fields = "__all__"


class ImageEvenementForm(ModelForm):
    class Meta:
        model = ImageEvenement
        fields = "__all__"


class CollectionObservationForm(ModelForm):
    class Meta:
        model = CollectionObservation
        fields = "__all__"


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"


class CaracteristiqueEvenementForm(ModelForm):
    class Meta:
        model = CaracteristiqueEvenement
        fields = "__all__"


class CaracteristiqueForm(ModelForm):
    class Meta:
        model = Caracteristique
        fields = "__all__"


class ImageObservationForm(ModelForm):
    class Meta:
        model = ImageObservation
        fields = "__all__"


class TypeEvenementForm(ModelForm):
    class Meta:
        model = TypeEvenement
        fields = ["nom", "abreviation"]
