# Generated by Django 2.2.7 on 2019-11-14 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
            preserve_default=False,
        ),
    ]
