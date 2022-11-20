import datetime
import tablib
from django.db import models
from django.utils import timezone
from import_export import resources

# TODO: Equipment class
# class Equipment(models.Model):
#     equipment_description = models.CharField(max_length=64, default='TBC')
#     equipment_maximo_tag = models.CharField(max_length=64, primary_key=True)
work_list = [
        ('Basket Transfers', 'Basket Transfers'),
        ('Bunkering Fuel and Base Oil', 'Bunkering Fuel and Base Oil'),
        ('Confined Space Entry', 'Confined Space Entry'),
        ('Crane Operations', 'Crane Operations'),
        ('Drilling', 'Drilling'),
        ('Managed Pressure Drilling', 'Managed Pressure Drilling'),
        ('Explosive Handling', 'Explosive Handling'),
        ('Helicopter Operations', 'Helicopter Operations'),
        ('Hot Work', 'Hot Work'),
        ('Man Riding Derrick', 'Man Riding Derrick'),
        ('Man Riding Moonpool', 'Man Riding Moonpool'),
        ('Pressure Testing', 'Pressure Testing'),
        ('Radioactive Handling', 'Radioactive Handling'),
        ('Supply Boat Operations', 'Supply Boat Operations'),
        ('Well Testing', 'Well Testing'),
        ('Wireline', 'Wireline'),
        ('Overside Work', 'Overside Work'),
        ('Running Marine Riser', 'Running Marine Riser'),
        ('ROV Operations', 'ROV Operations'),
        ('Riserless Drilling', 'Riserless Drilling'),
        ('Critical Ballast', 'Critical Ballast'),
    ]


class Restriction(models.Model):
    restriction = models.CharField(primary_key=True, max_length=3)
    restriction_details = models.CharField(max_length=200)
    is_self_restriction = models.BooleanField()

    def __unicode__(self):
        return str(self.restriction)


class SIMOPS(models.Model):
    work_type_1 = models.CharField(max_length=64, choices=work_list, blank=True)
    work_type_2 = models.CharField(max_length=64, choices=work_list, blank=True)
    are_conflicting = models.BooleanField()
    restriction = models.ForeignKey(Restriction, on_delete=models.PROTECT, db_column='restriction')

    def __str__(self):
        return f'{self.work_type_1} and {self.work_type_2} are resolved in {self.restriction}'

class PTW(models.Model):
    prefix = models.CharField(max_length=5, choices=[
        ('PTW', 'PTW'),
        ('HVPTW', 'HVPTW'),
        ('HVSFT', 'HVSFT'),
        ('Event', 'Event'),
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
    work_type = models.CharField(max_length=64, choices=work_list, blank=True)
    work_location = models.CharField(max_length=64, default='TBC')
    performing_authority = models.CharField(max_length=64, blank=True)
    permit_audit = models.IntegerField(default=0)

    def __str__(self):
        return f'PTW_{self.id}: {self.work_type} - {self.work_description} at' \
               f' {self.work_location} by {self.performing_authority} on {self.planned_work_at}'

    def check_conflicts(self):
        pass


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


def get_total_audits(timedelta):
    # gets total sum of permit audits for given number of days back
    moment_in_the_past = timezone.now() - datetime.timedelta(days=timedelta)
    data = PTW.objects.filter(created_at__gte=moment_in_the_past).values_list('permit_audit', flat=True)
    return sum(data)


def import_csv():
    with open('ptw/static/ptw/data/restrictions.csv', 'r') as fh:
        imported_data = tablib.Dataset().load(fh)
        resource = resources.modelresource_factory(model=SIMOPS)()
        result = resource.import_data(imported_data, dry_run=False)
        print(result.has_errors())
