# Generated by Django 2.2.1 on 2019-05-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
