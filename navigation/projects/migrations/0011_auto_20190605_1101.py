# Generated by Django 2.2.1 on 2019-06-05 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='project',
        ),
        migrations.AddField(
            model_name='map',
            name='activity',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='projects.Activity', verbose_name='activity'),
            preserve_default=False,
        ),
    ]
