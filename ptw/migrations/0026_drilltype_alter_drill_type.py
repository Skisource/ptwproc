# Generated by Django 4.1.2 on 2024-01-19 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0025_drill_long_description_drill_personnel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrillType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Abandon', 'Abandon'), ('Supervisor Missing', 'Supervisor Missing'), ('Lifeboat Launch', 'Lifeboat Launch'), ('Fire', 'Fire'), ('Liferaft', 'Liferaft'), ('Liferaft Davit & Inflation', 'Liferaft Davit & Inflation'), ('Alternate ECC', 'Alternate ECC'), ('Line Throwing', 'Line Throwing'), ('Ballast Control', 'Ballast Control'), ('Collision', 'Collision'), ('Heavy WX', 'Heavy WX'), ('Structural', 'Structural'), ('Grounding', 'Grounding'), ('DP Drill', 'DP Drill'), ('Blackout', 'Blackout'), ('Emergency Steering', 'Emergency Steering'), ('Gas H2S', 'Gas H2S'), ('Helideck Emergency', 'Helideck Emergency'), ('Rescue at Height', 'Rescue at Height'), ('MOB', 'MOB'), ('SOPEP', 'SOPEP'), ('Confined Space', 'Confined Space'), ('First Aid', 'First Aid'), ('ISPS', 'ISPS'), ('Well Control', 'Well Control')], max_length=32)),
                ('frequency', models.IntegerField(help_text='Drill frequency in days')),
            ],
        ),
        migrations.AlterField(
            model_name='drill',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptw.drilltype'),
        ),
    ]
