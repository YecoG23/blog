# Generated by Django 2.2.1 on 2019-05-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0013_remove_aula_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='slug',
            field=models.SlugField(blank=True, max_length=120),
        ),
    ]
