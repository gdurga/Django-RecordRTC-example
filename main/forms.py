from django import forms
from main.models import Audiofl

class AudioflForm(forms.ModelForm):
    class Meta:
        model = Audiofl
        fields = ('descricao', 'foto', )
        widgets = {'foto': forms.HiddenInput()}
