from django.db import models


class Funcao(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.descricao


class Funcionario(models.Model):
    cargo = models.ForeignKey(Funcao, on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=150)
    cpf = models.IntegerField('CPF')
    telefone = models.IntegerField('telefone')
    endereco = models.CharField('Endereço', max_length=200)
    salario = models.DecimalField('Salário', decimal_places=2, max_digits=7)
    data_admissao = models.DateField('Data da admissão')
    data_demissao = models.DateField('Data da demissão')

    def __str__(self):
        return self.nome
