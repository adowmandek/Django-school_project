# Generated by Django 3.2.4 on 2021-08-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='Event_atendee',
            field=models.IntegerField(blank=True, default=30, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='calender',
            name='Event_date',
            field=models.DateField(blank=True, default=25, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='calender',
            name='Event_duration',
            field=models.DateTimeField(blank=True, default=20, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='calender',
            name='Event_goal',
            field=models.CharField(blank=True, default=25, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='calender',
            name='Event_name',
            field=models.CharField(blank=True, default=28, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='calender',
            name='Event_signed_by',
            field=models.CharField(blank=True, default=34, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='calender',
            name='Event_venue',
            field=models.CharField(blank=True, default=23, max_length=10, null=True),
        ),
    ]
