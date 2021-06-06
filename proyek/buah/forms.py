from django import forms

from .models import TabelBuah

class TabelBuahForm(forms.ModelForm):
    class Meta:
        model = TabelBuah
        fields = '__all__'