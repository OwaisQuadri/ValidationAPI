# Generated by Django 3.2.9 on 2021-11-17 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_api', '0006_auto_20211116_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]