# Generated by Django 2.2.1 on 2019-05-07 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_aula_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aula',
            options={'ordering': ['creado', 'actualizado']},
        ),
        migrations.RemoveField(
            model_name='aula',
            name='publicado_en',
        ),
    ]