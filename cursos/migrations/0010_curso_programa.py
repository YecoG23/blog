# Generated by Django 2.2.1 on 2019-05-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0009_aula_archivos'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='programa',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]