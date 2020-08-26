# Generated by Django 3.1 on 2020-08-22 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('telefone', models.IntegerField(verbose_name='telefone')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Salário')),
                ('data_admissao', models.DateField(verbose_name='Data da admissão')),
                ('data_demissao', models.DateField(verbose_name='Data da demissão')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.funcao')),
            ],
        ),
    ]