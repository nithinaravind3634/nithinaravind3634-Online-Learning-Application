# Generated by Django 5.1.5 on 2025-01-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentusername', models.CharField(max_length=20)),
                ('studentemail', models.EmailField(max_length=254)),
                ('studentphone', models.CharField(max_length=10)),
                ('studentpassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='teachermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherusername', models.CharField(max_length=20)),
                ('teacheremail', models.EmailField(max_length=254)),
                ('teacherphone', models.CharField(max_length=10)),
                ('teacherpassword', models.CharField(max_length=20)),
            ],
        ),
    ]
