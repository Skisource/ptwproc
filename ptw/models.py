from django.db import models
from django.utils import timezone

# TODO: Equipment class
# class Equipment(models.Model):
#     equipment_description = models.CharField(max_length=64, default='TBC')
#     equipment_maximo_tag = models.CharField(max_length=64, primary_key=True)


class PTW(models.Model):
    prefix = models.CharField(max_length=5, choices=[
        ('PTW', 'PTW'),
        ('HVPTW', 'HVPTW'),
        ('HVSFT', 'HVSFT'),
    ], default='PTW')
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=10, choices=[
        ('created', 'created'),
        ('authorized', 'authorized'),
        ('suspended', 'suspended'),
        ('closed', 'closed'),
        ('cancelled', 'cancelled')]
                              )
    created_at = models.DateTimeField(default=timezone.now)
    authorized_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(default=timezone.now)
    planned_work_at = models.DateTimeField(default=timezone.now)
    work_description = models.CharField(max_length=64, default='TBC')
    # TODO: work types as per SIMOPS restriction matrix
    work_type = models.CharField(max_length=64, blank=True, choices=[
        ('Basket Transfers', 'Basket Transfers'),
        ('Bunkering (Fuel and Base Oil)', 'Bunkering (Fuel and Base Oil)'),
        ('Confined Space Entry', 'Confined Space Entry'),
        ('Crane Operations', 'Crane Operations'),
        ('Drilling', 'Drilling'),
        ('Managed Pressure Drilling', 'Managed Pressure Drilling'),
        ('Explosive Handling', 'Explosive Handling'),
        ('Helicopter Operations', 'Helicopter Operations'),
        ('Hot Work', 'Hot Work'),
        ('Man Riding - Derrick', 'Man Riding - Derrick'),
        ('Man Riding – Moonpool', 'Man Riding – Moonpool'),
        ('Pressure Testing', 'Pressure Testing'),
        ('Radioactive Handling', 'Radioactive Handling'),
        ('Supply Boat Operations', 'Supply Boat Operations'),
        ('Well Testing', 'Well Testing'),
        ('Wireline', 'Wireline'),
        ('Over the Side Work', 'Over the Side Work'),
        ('Running Marine Riser', 'Running Marine Riser'),
        ('ROV Operations', 'ROV Operations'),
        ('Riserless Drilling', 'Riserless Drilling'),
        ('Critical Ballast', 'Critical Ballast'),
    ])
    work_location = models.CharField(max_length=64, default='TBC')
    performing_authority = models.CharField(max_length=64, blank=True)
    permit_audit = models.IntegerField(default=0)

    def __str__(self):
        return f'PTW_{self.id}: {self.work_type} - {self.work_description} at' \
               f' {self.work_location} by {self.performing_authority} on {self.planned_work_at}'

    def check_conflicts(self):
        pass
#     TODO: conflict check function as per SIMOPS restriction matrix

#     As follows:
# id::charfield
# operation_activity::charfield
# paired_operation_activity::charfield
# conflict_type::charfield или conflict_type_id (foreign key в таблице, где список конфликтов)
# типа сделать таблицу conflict_type:
# id::charfield
# conflict_type::charfield
# description::charfield
#
# а, у тебя даже есть название для типа конфликта
# restriction
# restriction_type, restriction_id


class Isolation(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=10, choices=[
        ('created', 'created'),
        ('authorized', 'authorized'),
        ('long term', 'long term'),
        ('closed', 'closed'),
        ('cancelled', 'cancelled')], default='created')
    created_at = models.DateTimeField(default=timezone.now)
    isolation_type = models.CharField(max_length=24, choices=[
        ('electrical', 'electrical'),
        ('mechanical', 'mechanical'),
        ('electrical & mechanical', 'electrical & mechanical')
    ], default='electrical')
    performing_authority = models.CharField(max_length=24, default='TBC')
    authorized_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(default=timezone.now)
    equipment_description = models.CharField(max_length=24, default='TBC')
    equipment_maximo_tag = models.CharField(max_length=24, default='TBC')


class SafeEntry(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=10, choices=[
        ('created', 'created'),
        ('authorized', 'authorized'),
        ('closed', 'closed'),
        ('cancelled', 'cancelled')
    ], default='created')
    created_at = models.DateTimeField(default=timezone.now)
    performing_authority = models.CharField(max_length=24, default='TBC')
    authorized_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(default=timezone.now)
    space_description = models.CharField(max_length=24, default='TBC')
    space_maximo_tag = models.CharField(max_length=24, default='TBC')


class Inhibit(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=10, choices=[
        ('created', 'created'),
        ('authorized', 'authorized'),
        ('closed', 'closed'),
        ('cancelled', 'cancelled')
    ], default='created')
    created_at = models.DateTimeField(default=timezone.now)
    performing_authority = models.CharField(max_length=24, default='TBC')
    authorized_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(default=timezone.now)
    system_description = models.CharField(max_length=24, default='TBC')
    system_maximo_tag = models.CharField(max_length=24, default='TBC')
    ias_tags = models.CharField(max_length=60, default='TBC')
    block_or_suppress = models.CharField(max_length=10, choices=[
        ('block', 'block'),
        ('suppress', 'suppress')
    ], default='block')
    location = models.CharField(max_length=60, default='TBC')
    work_description = models.CharField(max_length=60, default='TBC')
    related_tags = models.CharField(max_length=60, default='TBC')


class Restriction(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    restriction_details = models.CharField(max_length=200)
    is_self_restriction = models.BooleanField()


