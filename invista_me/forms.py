from pyexpat import model
from django.forms import ModelForm
from .models import Investimentos

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimentos
        fields = '__all__'