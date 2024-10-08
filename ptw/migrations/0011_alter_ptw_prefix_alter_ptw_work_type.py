# Generated by Django 4.1.2 on 2022-11-20 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0010_alter_simops_work_type_1_alter_simops_work_type_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptw',
            name='prefix',
            field=models.CharField(choices=[('PTW', 'PTW'), ('HVPTW', 'HVPTW'), ('HVSFT', 'HVSFT'), ('Event', 'Event')], default='PTW', max_length=5),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='work_type',
            field=models.ForeignKey(db_column='work_type_1', on_delete=django.db.models.deletion.PROTECT, to='ptw.simops'),
        ),
    ]
