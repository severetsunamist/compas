# Generated by Django 4.1.7 on 2023-09-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0003_rename_owner_name_flat_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='lat',
            field=models.CharField(default='34.343434', max_length=12, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='lng',
            field=models.CharField(default='36.343434', max_length=12, verbose_name='Долгота'),
        ),
    ]
