# Generated by Django 4.1.2 on 2022-11-21 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0013_alter_simops_restriction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simops',
            name='restriction',
            field=models.ForeignKey(db_column='restriction', on_delete=django.db.models.deletion.PROTECT, to='ptw.restriction'),
        ),
    ]
