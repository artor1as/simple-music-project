# Generated by Django 2.0.1 on 2018-01-20 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discovery', '0002_auto_20171114_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discovery',
            options={'ordering': ['order'], 'verbose_name_plural': 'Discoveries'},
        ),
    ]