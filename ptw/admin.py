from symbol import pass_stmt

from django.contrib import admin
from .models import PTW, Location, Inhibit, Isolation, SafeEntry, Restriction, SIMOPS, DrillType, Drill


class PTWAdmin(admin.ModelAdmin):
    list_display = ('prefix', 'id', 'created_at', 'performing_authority',
                    'work_type', 'work_location', 'status', 'permit_audit')
    list_filter = ['created_at']
    search_fields = ['id', 'status', 'work_type', 'work_location']


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'x', 'y')
    list_filter = ['name']
    search_fields = ['name']


class IsolationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'isolation_type', 'performing_authority', 'equipment_description', 'status')
    list_filter = ['created_at']
    search_fields = ['id', 'status', 'equipment_description']


class SafeEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'performing_authority', 'space_description', 'status')
    list_filter = ['created_at']
    search_fields = ['id', 'status', 'space_description']


class InhibitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'performing_authority', 'system_description', 'ias_tags', 'block_or_suppress', 'location',
        'work_description', 'related_tags', 'status')
    list_filter = ['created_at']
    search_fields = ['id', 'status', 'ias_tags']


class RestrictionAdmin(admin.ModelAdmin):
    list_display = ('restriction', 'restriction_details', 'is_self_restriction')


class SIMOPSAdmin(admin.ModelAdmin):
    list_display = ('work_type_1', 'work_type_2', 'are_conflicting', 'restriction')


class DrillTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'frequency')

class DrillAdmin(admin.ModelAdmin):
    list_display = ('type', 'date', 'date_next', 'description', 'long_description', 'personnel')
    list_filter = ['date']
    search_fields = ['date', 'type', 'description']


# Register your models here.
admin.site.register(PTW, PTWAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Isolation, IsolationAdmin)
admin.site.register(Inhibit, InhibitAdmin)
admin.site.register(SafeEntry, SafeEntryAdmin)
admin.site.register(Restriction, RestrictionAdmin)
admin.site.register(SIMOPS, SIMOPSAdmin)
admin.site.register(DrillType, DrillTypeAdmin)
admin.site.register(Drill, DrillAdmin)
