# Generated by Django 5.1.5 on 2025-02-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnapp', '0004_alter_postfilemodel_fileupload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfilemodel',
            name='fileupload',
            field=models.FileField(blank=True, null=True, upload_to='learnapp/static/files/'),
        ),
        migrations.AlterField(
            model_name='postvideomodel',
            name='videoupload',
            field=models.FileField(blank=True, null=True, upload_to='learnapp/static/videos/'),
        ),
    ]
