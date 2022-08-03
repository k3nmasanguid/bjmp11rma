from django.contrib import admin
from rma.models import PersonalInfo, PresentAddress, PermanentAddress, Spouse, Father, Mother,Sibling, Children, Primary

class PersonalInfoAdmin(admin.ModelAdmin):
    model = PersonalInfo
    list_display = ['user', 'last_name','first_name','middle_name','suffix', 'gender','civil_status','date_of_birth','cellphone_no']
    list_filter = ['gender','civil_status']
    search_fields = ['user','last_name','first_name','middle_name']
    ordering = ['last_name']
    filter_horizontal = ()
admin.site.register(PersonalInfo,PersonalInfoAdmin)
admin.site.register(PresentAddress)
admin.site.register(PermanentAddress)
admin.site.register(Spouse)
admin.site.register(Father)
admin.site.register(Mother)
admin.site.register(Sibling)
admin.site.register(Children)
admin.site.register(Primary)
