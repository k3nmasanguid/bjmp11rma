from django.contrib import admin
from upload_docs.models import PDS, TOR, CAV, Diploma, BirthCert, EligibilityDoc, MarriageCert, Sketch, Barangay, NBI, Police, Fiscal, MTC, RTC, PNPDI

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
########
class EligibilityDocAdmin(admin.ModelAdmin):
    model = EligibilityDoc
    list_display = ['user', 'eligibility_doc','uploaded_at']

class MarriageCertAdmin(admin.ModelAdmin):
    model = MarriageCert
    list_display = ['user', 'marriage_cert','uploaded_at']

class SketchAdmin(admin.ModelAdmin):
    model = Sketch
    list_display = ['user', 'sketch','uploaded_at']

class BarangayAdmin(admin.ModelAdmin):
    model = Barangay
    list_display = ['user', 'barangay','uploaded_at']

class NBIAdmin(admin.ModelAdmin):
    model = NBI
    list_display = ['user', 'nbi','uploaded_at']

class PoliceAdmin(admin.ModelAdmin):
    model = Police
    list_display = ['user', 'police','uploaded_at']

class FiscalAdmin(admin.ModelAdmin):
    model = Fiscal
    list_display = ['user', 'fiscal','uploaded_at']

class MTCAdmin(admin.ModelAdmin):
    model = MTC
    list_display = ['user', 'mtc','uploaded_at']

class RTCAdmin(admin.ModelAdmin):
    model = RTC
    list_display = ['user', 'rtc','uploaded_at']

class PNPDIAdmin(admin.ModelAdmin):
    model = PNPDI
    list_display = ['user', 'pnpdi','uploaded_at']

admin.site.register(PDS, PDSAdmin)
admin.site.register(TOR, TORAdmin)
admin.site.register(CAV, CAVAdmin)
admin.site.register(Diploma, DiplomaAdmin)
admin.site.register(BirthCert, BirthCertAdmin)
admin.site.register(EligibilityDoc,EligibilityDocAdmin)
admin.site.register(MarriageCert,MarriageCertAdmin)
admin.site.register(Sketch,SketchAdmin)
admin.site.register(Barangay,BarangayAdmin)
admin.site.register(NBI,NBIAdmin)
admin.site.register(Police,PoliceAdmin)
admin.site.register(Fiscal,FiscalAdmin)
admin.site.register(MTC,MTCAdmin)
admin.site.register(RTC,RTCAdmin)
admin.site.register(PNPDI,PNPDIAdmin)
