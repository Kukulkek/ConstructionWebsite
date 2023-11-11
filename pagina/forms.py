from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class MaterialSearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=False)