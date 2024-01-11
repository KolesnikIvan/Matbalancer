from django.contrib import admin

from infr_app.models import DO, Field, FloodingObject, Pad, Prognose, SeparationObject, Well

class DNSAdminView(admin.ModelAdmin):
    list_display = ['name', 'obj_type', 'liq_sep_pwr', 'field'] #'oil_sep_pwr', 'wat_sep_pwr', 'liq_pmp_pwr', 'oil_pmp_pwr', 'wat_pmp_pwr', 'wcut', 'field']
    list_display_links = ['field']

class PadAdminView(admin.ModelAdmin):
    list_display = ['name', 'field', 'oil_fact', 'liq_fact', 'gas_fact', 'fld_fact']
    list_display_links = ['field']

class WellAdminView(admin.ModelAdmin):
    list_display = ['name', 'pad'] #, 'pad.field']
    list_display_link = ['pad']#.field']

class FieldAdminView(admin.ModelAdmin):
    list_display = ['name', 'do']
    list_display_link = ['do']

# Register your models here.
admin.site.register(DO)
admin.site.register(Field, FieldAdminView)
admin.site.register(SeparationObject, DNSAdminView)
admin.site.register(FloodingObject)
admin.site.register(Pad, PadAdminView)
admin.site.register(Well, WellAdminView)
admin.site.register(Prognose)
