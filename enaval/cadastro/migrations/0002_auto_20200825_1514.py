# Generated by Django 3.1 on 2020-08-25 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.funcao'),
        ),
    ]
