# Generated by Django 3.2.9 on 2021-11-12 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_advert_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='author',
            new_name='seller',
        ),
    ]
