# Generated by Django 2.2 on 2019-04-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190410_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_map',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
