from django.contrib import admin
from upload_docs.models import PDS, TOR, CAV, Diploma, BirthCert

class PDSAdmin(admin.ModelAdmin):
    model = PDS
    list_display = ['user', 'pds','uploaded_at']

class TORAdmin(admin.ModelAdmin):
    model = TOR
    list_display = ['user', 'tor','uploaded_at']

class CAVAdmin(admin.ModelAdmin):
    model = CAV
    list_display = ['user', 'cav','uploaded_at']

class DiplomaAdmin(admin.ModelAdmin):
    model = Diploma
    list_display = ['user', 'diploma','uploaded_at']


class BirthCertAdmin(admin.ModelAdmin):
    model = BirthCert
    list_display = ['user', 'birthcert','uploaded_at']

admin.site.register(PDS, PDSAdmin)
admin.site.register(TOR, TORAdmin)
admin.site.register(CAV, CAVAdmin)
admin.site.register(Diploma, DiplomaAdmin)
admin.site.register(BirthCert, BirthCertAdmin)
