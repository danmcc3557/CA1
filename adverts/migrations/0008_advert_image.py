# Generated by Django 3.2.9 on 2021-11-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0007_alter_advert_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(blank=True, upload_to='advert'),
        ),
    ]
