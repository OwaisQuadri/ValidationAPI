# Generated by Django 3.2.9 on 2021-11-16 07:38

from django.db import migrations, models
import face_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('face_api', '0005_alter_face_face'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='face',
            field=models.ImageField(upload_to=face_api.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='face',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
