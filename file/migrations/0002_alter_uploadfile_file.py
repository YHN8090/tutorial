# Generated by Django 3.2.5 on 2022-05-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
