from django.forms import ModelForm
from .models import Transacao
class PostForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'tipo_transacao']


        