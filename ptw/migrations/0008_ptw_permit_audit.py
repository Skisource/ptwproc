# Generated by Django 4.1.2 on 2022-11-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0007_alter_ptw_work_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ptw',
            name='permit_audit',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
