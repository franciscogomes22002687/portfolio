# Generated by Django 4.0.4 on 2023-06-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_projeto_link_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc',
            name='linkGithub',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='tfc',
            name='linkYoutube',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='tfc',
            name='relatorio',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
