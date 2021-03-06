# Generated by Django 3.0.8 on 2020-07-14 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(verbose_name='Código')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoFornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.CharField(max_length=150, verbose_name='Fornecedor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demoapp.Produto', verbose_name='Produto')),
            ],
        ),
    ]
