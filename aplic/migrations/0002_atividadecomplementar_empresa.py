# Generated by Django 2.2.19 on 2021-04-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividadecomplementar',
            name='empresa',
            field=models.CharField(default='null', max_length=55, verbose_name='Empresa/Instituição'),
            preserve_default=False,
        ),
    ]
