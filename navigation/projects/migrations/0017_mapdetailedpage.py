# Generated by Django 2.2.1 on 2019-06-09 02:08

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20190608_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapDetailedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(default='', max_length=100)),
                ('map_data', jsonfield.fields.JSONField()),
                ('project', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='project')),
            ],
        ),
    ]
