# Generated by Django 2.2.1 on 2019-05-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_auto_20190509_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='banner_img',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='ciclo_academico',
            field=models.CharField(blank=True, max_length=120, verbose_name='Ciclo academico'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='num_credito',
            field=models.PositiveIntegerField(blank=True, verbose_name='Numero de creditos'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='pre_requisito',
            field=models.CharField(blank=True, max_length=120, verbose_name='Pre requisitos'),
        ),
    ]