# Generated by Django 4.1.2 on 2022-11-08 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ptw', '0002_remove_ptw_approved_at_remove_ptw_approved_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Isolation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SafeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='ptw',
            name='authorized_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='closed_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='performing_authority',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='planned_work_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('approved', 'approved'), ('authorized', 'authorized'), ('suspended', 'suspended'), ('closed', 'closed'), ('cancelled', 'cancelled')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ptw',
            name='work_type',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
