from django.contrib import admin
from rma.models import PersonalInfo, PresentAddress, PermanentAddress, Spouse, Father, Mother,Sibling, Children, Primary, SeniorHigh, HighSchool, College, Graduate, Eligibility, Quota

class PersonalInfoAdmin(admin.ModelAdmin):
    model = PersonalInfo
    list_display = ['user', 'last_name','first_name','middle_name','suffix', 'gender','civil_status','date_of_birth','cellphone_no']
    list_filter = ['gender','civil_status']
    search_fields = ['user','last_name','first_name','middle_name']
    ordering = ['last_name']
    filter_horizontal = ()

class CollegeAdmin(admin.ModelAdmin):
    model = College
    list_display = ['user','school_name','course','year_from','year_to','units_earned','year_graduated','academic_honors']

class EligibilityAdmin(admin.ModelAdmin):
    model = Eligibility
    list_display = ['user','eligibility','rating','date_of_exam','place_of_exam','license']

admin.site.register(PersonalInfo,PersonalInfoAdmin)
admin.site.register(PresentAddress)
admin.site.register(PermanentAddress)
admin.site.register(Spouse)
admin.site.register(Father)
admin.site.register(Mother)
admin.site.register(Sibling)
admin.site.register(Children)
admin.site.register(Primary)
admin.site.register(HighSchool)
admin.site.register(SeniorHigh)
admin.site.register(College,CollegeAdmin)
admin.site.register(Graduate)
admin.site.register(Eligibility,EligibilityAdmin)

class QuotaAdmin(admin.ModelAdmin):
    model = Quota
    list_display = ['batch', 'status']

admin.site.register(Quota, QuotaAdmin)
