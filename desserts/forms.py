# forms.py
from django import forms
from django.forms import SelectMultiple
from .models import Dessert


class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = "__all__"
        widgets = {
            "locale_name_add": SelectMultiple,
            "additional_ingredient": SelectMultiple,
            "category_add": SelectMultiple,
        }
