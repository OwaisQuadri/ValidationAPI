# Generated by Django 3.2.9 on 2021-11-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_api', '0007_alter_face_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
