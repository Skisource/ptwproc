from django.contrib import admin
from .models import PTW, Inhibit, Isolation, SafeEntry, Restriction


class PTWAdmin(admin.ModelAdmin):
    list_display = ('prefix', 'id', 'created_at', 'performing_authority',
                    'work_type', 'work_location', 'status', 'permit_audit')
    list_filter = ['created_at']
    search_fields = ['id', 'status', 'work_type', 'work_location']


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
    list_display = ('id', 'restriction_details', 'is_self_restriction')


# Register your models here.
admin.site.register(PTW, PTWAdmin)
admin.site.register(Isolation, IsolationAdmin)
admin.site.register(Inhibit, InhibitAdmin)
admin.site.register(SafeEntry, SafeEntryAdmin)
admin.site.register(Restriction, RestrictionAdmin)
