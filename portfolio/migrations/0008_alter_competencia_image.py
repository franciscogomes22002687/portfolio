# Generated by Django 4.0.4 on 2022-07-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_competencia_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencia',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/skill_images'),
        ),
    ]
