# Generated by Django 4.1.2 on 2022-11-19 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0008_ptw_permit_audit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restriction',
            old_name='id',
            new_name='restriction',
        ),
        migrations.AlterField(
            model_name='ptw',
            name='permit_audit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='work_type',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.CreateModel(
            name='SIMOPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type_1', models.CharField(blank=True, choices=[('Basket Transfers', 'Basket Transfers'), ('Bunkering (Fuel and Base Oil)', 'Bunkering (Fuel and Base Oil)'), ('Confined Space Entry', 'Confined Space Entry'), ('Crane Operations', 'Crane Operations'), ('Drilling', 'Drilling'), ('Managed Pressure Drilling', 'Managed Pressure Drilling'), ('Explosive Handling', 'Explosive Handling'), ('Helicopter Operations', 'Helicopter Operations'), ('Hot Work', 'Hot Work'), ('Man Riding - Derrick', 'Man Riding - Derrick'), ('Man Riding – Moonpool', 'Man Riding – Moonpool'), ('Pressure Testing', 'Pressure Testing'), ('Radioactive Handling', 'Radioactive Handling'), ('Supply Boat Operations', 'Supply Boat Operations'), ('Well Testing', 'Well Testing'), ('Wireline', 'Wireline'), ('Over the Side Work', 'Over the Side Work'), ('Running Marine Riser', 'Running Marine Riser'), ('ROV Operations', 'ROV Operations'), ('Riserless Drilling', 'Riserless Drilling'), ('Critical Ballast', 'Critical Ballast')], max_length=64)),
                ('work_type_2', models.CharField(blank=True, choices=[('Basket Transfers', 'Basket Transfers'), ('Bunkering (Fuel and Base Oil)', 'Bunkering (Fuel and Base Oil)'), ('Confined Space Entry', 'Confined Space Entry'), ('Crane Operations', 'Crane Operations'), ('Drilling', 'Drilling'), ('Managed Pressure Drilling', 'Managed Pressure Drilling'), ('Explosive Handling', 'Explosive Handling'), ('Helicopter Operations', 'Helicopter Operations'), ('Hot Work', 'Hot Work'), ('Man Riding - Derrick', 'Man Riding - Derrick'), ('Man Riding – Moonpool', 'Man Riding – Moonpool'), ('Pressure Testing', 'Pressure Testing'), ('Radioactive Handling', 'Radioactive Handling'), ('Supply Boat Operations', 'Supply Boat Operations'), ('Well Testing', 'Well Testing'), ('Wireline', 'Wireline'), ('Over the Side Work', 'Over the Side Work'), ('Running Marine Riser', 'Running Marine Riser'), ('ROV Operations', 'ROV Operations'), ('Riserless Drilling', 'Riserless Drilling'), ('Critical Ballast', 'Critical Ballast')], max_length=64)),
                ('are_conflicting', models.BooleanField()),
                ('restriction', models.ForeignKey(db_column='restriction', on_delete=django.db.models.deletion.PROTECT, to='ptw.restriction')),
            ],
        ),
    ]
