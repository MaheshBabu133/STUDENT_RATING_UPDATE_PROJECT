# Generated by Django 4.1.7 on 2023-06-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_coding_comunication_theory_studentrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrating',
            name='cname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrating',
            name='coding',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrating',
            name='comminication',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrating',
            name='theory',
            field=models.CharField(max_length=100),
        ),
    ]