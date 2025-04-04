# Generated by Django 5.1.5 on 2025-02-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnapp', '0008_remove_postfilemodel_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfilemodel',
            name='filethumbnail',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='postfilemodel',
            name='filedescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postvideomodel',
            name='videodescription',
            field=models.TextField(),
        ),
    ]
