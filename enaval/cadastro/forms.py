from django import forms
from .models import Funcionario


class FunciForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"


class LoginForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=150)
    senha = forms.CharField(label='Senha', max_length=10)
