# Generated by Django 3.2.4 on 2021-08-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Trainer',
            field=models.CharField(blank=True, default=34, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Unit_Name',
            field=models.CharField(blank=True, default=31, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_material',
            field=models.FileField(blank=True, default=20, max_length=10, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, default=21, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='id_Number',
            field=models.CharField(blank=True, default=38, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='presentations',
            field=models.CharField(blank=True, default=30, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='profession',
            field=models.CharField(blank=True, default=32, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='results',
            field=models.PositiveSmallIntegerField(blank=True, default=22, max_length=10, null=True),
        ),
    ]
