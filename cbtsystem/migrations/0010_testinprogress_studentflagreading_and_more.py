# Generated by Django 4.0.4 on 2022-05-13 10:30

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cbtsystem', '0009_rename_settest_grouptest'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinprogress',
            name='studentFlagReading',
            field=jsonfield.fields.JSONField(default={}, null=True),
        ),
        migrations.AddField(
            model_name='testinprogress',
            name='studentFlagWriting',
            field=jsonfield.fields.JSONField(default={}, null=True),
        ),
    ]
