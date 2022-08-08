

from django.shortcuts import get_object_or_404, render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rma.models import Graduate, PermanentAddress, PersonalInfo, PresentAddress, Spouse, Father, Mother, Sibling, Children, Primary, HighSchool, SeniorHigh, College, Graduate, Eligibility
from rma.forms import PersonalInfoForm, PresentAddressForm, PermanentAddressForm, SpouseForm, FatherForm, MotherForm, SiblingForm, ChildrenForm, PrimaryForm, HighSchoolForm, SeniorHighForm, CollegeForm, GraduateForm, EligibilityForm

from upload_docs.models import PDS, TOR, CAV, Diploma, BirthCert, EligibilityDoc, MarriageCert, Sketch, Waiver, Barangay, NBI, Police, Fiscal, MTC, RTC, PNPDI
from upload_docs.forms import PDSForm, TORForm, CAVForm, DiplomaForm, BirthCertForm, EligibilityDocForm, MarriageCertForm, SketchForm, WaiverForm, BarangayForm, NBIForm,PoliceForm,FiscalForm,MTCForm,RTCForm, PNPDIForm

def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None



############################################################### LOADED DATA IN HOME #########################################################################

@login_required()
def home(request):
    return render(request, 'home.html') 

@login_required()  
def personal_info_data(request):
    obj_pinfo = get_or_none(PersonalInfo, user_id=request.user)
    return render(request, 'loaded_data/personal_info_data.html',{'obj_pinfo':obj_pinfo})

@login_required()
def present_address_data(request):
    obj_present_address = get_or_none(PresentAddress, user_id=request.user)
    return render(request, 'loaded_data/present_address_data.html',{'obj_present_address':obj_present_address})

@login_required()
def permanent_address_data(request):
    obj_permanent_address = get_or_none(PermanentAddress, user_id=request.user)
    return render(request, 'loaded_data/permanent_address_data.html',{'obj_permanent_address':obj_permanent_address})

############################################################### END LOADED DATA IN HOME ######################################################################



############################################################### LOAD MODAL IN HOME PAGE ######################################################################

@login_required()
def personal_info(request):
    try:
        obj = request.user.personalinfo
    except ObjectDoesNotExist:
        obj = PersonalInfo(user=request.user)

    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'personal_info'})
    else:
        form = PersonalInfoForm(instance=obj)
    return render(request, 'modals/personal_info_modal.html',{'form':form})

@login_required()
def present_address(request):
    try:
        obj = request.user.presentaddress
    except ObjectDoesNotExist:
        obj = PresentAddress(user=request.user)

    if request.method == 'POST':
        form = PresentAddressForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'present_address'})
    else:
        form = PresentAddressForm(instance=obj)  
    return render(request, 'modals/present_address_modal.html',{'form':form})

@login_required()
def permanent_address(request):
    try:
        obj = request.user.permanentaddress
    except ObjectDoesNotExist:
        obj = PermanentAddress(user=request.user)

    if request.method == 'POST':
        form = PermanentAddressForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'permanent_address'})
    else:
        form = PermanentAddressForm(instance=obj)  
    return render(request, 'modals/permanent_address_modal.html',{'form':form})

############################################################### END LOAD MODAL IN HOME PAGE ######################################################################


############################################################### LOADED DATA IN BACKGROUND PAGE #########################################################################

@login_required()
def background(request):
    return render(request, 'background.html')

@login_required()
def spouse_data(request):
    obj_spouse = get_or_none(Spouse, user_id=request.user)
    return render(request, 'loaded_data/spouse_data.html',{'obj_spouse':obj_spouse})

@login_required()
def father_data(request):
    obj_father = get_or_none(Father, user_id=request.user)
    return render(request, 'loaded_data/father_data.html',{'obj_father':obj_father})

@login_required()
def mother_data(request):
    obj_mother = get_or_none(Mother, user_id=request.user)
    return render(request, 'loaded_data/mother_data.html',{'obj_mother':obj_mother})

@login_required()
def sibling_data(request):
    obj_sibling = Sibling.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/sibling_data.html',{'obj_sibling':obj_sibling})


@login_required()
def children_data(request):
    obj_children = Children.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/children_data.html',{'obj_children':obj_children})

############################################################### END LOADED DATA IN BACKGROUND PAGE #########################################################################

###############################################################  LOAD MODAL IN BACKGROUND PAGE ######################################################################

@login_required()
def spouse(request):
    try:
        obj = request.user.spouse
    except ObjectDoesNotExist:
        obj = Spouse(user=request.user)

    if request.method == 'POST':
        form = SpouseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'spouse'})
    else:
        form = SpouseForm(instance=obj)  
    return render(request, 'modals/spouse_modal.html',{'form':form})

@login_required()
def father(request):
    try:
        obj = request.user.father
    except ObjectDoesNotExist:
        obj = Father(user=request.user)

    if request.method == 'POST':
        form = FatherForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'father'})
    else:
        form = FatherForm(instance=obj)  
    return render(request, 'modals/father_modal.html',{'form':form})

@login_required()
def mother(request):
    try:
        obj = request.user.mother
    except ObjectDoesNotExist:
        obj = Mother(user=request.user)

    if request.method == 'POST':
        form = MotherForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'mother'})
    else:
        form = MotherForm(instance=obj)  
    return render(request, 'modals/mother_modal.html',{'form':form})

@login_required()
def sibling(request):
    if request.method == 'POST':
        form = SiblingForm(request.POST)
        if form.is_valid():
            sibling = form.save(commit=False)
            sibling.user_id = request.user.id
            sibling.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'sibling'})
    else:
        form = SiblingForm()  
    return render(request, 'modals/sibling_modal.html',{'form':form})

@login_required()
def sibling_edit(request, id):
    obj = get_object_or_404(Sibling, id=id)

    if request.method == 'POST':
        form = SiblingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'sibling'})
    else:
        form = SiblingForm(instance=obj)  
    return render(request, 'modals/sibling_modal.html',{'form':form})


@login_required()
def sibling_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Sibling, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'sibling'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def children(request):
    if request.method == 'POST':
        form = ChildrenForm(request.POST)
        if form.is_valid():
            children = form.save(commit=False)
            children.user_id = request.user.id
            children.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'children'})
    else:
        form = ChildrenForm()  
    return render(request, 'modals/children_modal.html',{'form':form})

@login_required()
def children_edit(request, id):
    obj = get_object_or_404(Children, id=id)

    if request.method == 'POST':
        form = ChildrenForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'children'})
    else:
        form = ChildrenForm(instance=obj)  
    return render(request, 'modals/children_modal.html',{'form':form})


@login_required()
def children_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Children, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'children'}) 
    else:
        return render(request, 'modals/delete_modal.html')

###############################################################  END LOAD MODAL IN BACKGROUND PAGE ######################################################################


############################################################### LOADED DATA IN EDUCATION PAGE #########################################################################

@login_required()
def education(request):
    return render(request, 'education.html')

@login_required()
def primary_data(request):
    obj_primary = Primary.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/primary_data.html', {'obj_primary':obj_primary})

@login_required()
def high_school_data(request):
    obj_high_school = HighSchool.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/high_school_data.html', {'obj_high_school':obj_high_school})

@login_required()
def senior_high_data(request):
    obj_senior_high = SeniorHigh.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/senior_high_data.html', {'obj_senior_high':obj_senior_high})

@login_required()
def college_data(request):
    obj_college = College.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/college_data.html', {'obj_college':obj_college})

@login_required()
def graduate_data(request):
    obj_graduate = Graduate.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/graduate_data.html', {'obj_graduate':obj_graduate})

############################################################### END LOADED DATA IN EDUCATION PAGE #########################################################################


############################################################### LOAD MODAL IN EDUCATION PAGE ######################################################################
@login_required()
def primary(request):
    if request.method == 'POST':
        form = PrimaryForm(request.POST)
        if form.is_valid():
            primary = form.save(commit=False)
            primary.user_id = request.user.id
            primary.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'primary'})
    else:
        form = PrimaryForm()  
    return render(request, 'modals/primary_modal.html',{'form':form})

@login_required()
def primary_edit(request, id):
    obj = get_object_or_404(Primary, id=id)

    if request.method == 'POST':
        form = PrimaryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'primary'})
    else:
        form = PrimaryForm(instance=obj)  
    return render(request, 'modals/primary_modal.html',{'form':form})


@login_required()
def primary_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Primary, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'primary'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def high_school(request):
    if request.method == 'POST':
        form = HighSchoolForm(request.POST)
        if form.is_valid():
            high_school = form.save(commit=False)
            high_school.user_id = request.user.id
            high_school.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'high_school'})
    else:
        form = HighSchoolForm()  
    return render(request, 'modals/high_school_modal.html',{'form':form})

@login_required()
def high_school_edit(request, id):
    obj = get_object_or_404(HighSchool, id=id)

    if request.method == 'POST':
        form = HighSchoolForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'high_school'})
    else:
        form = HighSchoolForm(instance=obj)  
    return render(request, 'modals/high_school_modal.html',{'form':form})


@login_required()
def high_school_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(HighSchool, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'high_school'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def senior_high(request):
    if request.method == 'POST':
        form = SeniorHighForm(request.POST)
        if form.is_valid():
            senior_high = form.save(commit=False)
            senior_high.user_id = request.user.id
            senior_high.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'senior_high'})
    else:
        form = SeniorHighForm()  
    return render(request, 'modals/senior_high_modal.html',{'form':form})

@login_required()
def senior_high_edit(request, id):
    obj = get_object_or_404(SeniorHigh, id=id)

    if request.method == 'POST':
        form = SeniorHighForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'senior_high'})
    else:
        form = SeniorHighForm(instance=obj)  
    return render(request, 'modals/senior_high_modal.html',{'form':form})


@login_required()
def senior_high_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(SeniorHigh, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'senior_high'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.save(commit=False)
            college.user_id = request.user.id
            college.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm()  
    return render(request, 'modals/college_modal.html',{'form':form})

@login_required()
def college_edit(request, id):
    obj = get_object_or_404(College, id=id)

    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm(instance=obj)  
    return render(request, 'modals/college_modal.html',{'form':form})


@login_required()
def college_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(College, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'college'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.save(commit=False)
            college.user_id = request.user.id
            college.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm()  
    return render(request, 'modals/college_modal.html',{'form':form})

@login_required()
def college_edit(request, id):
    obj = get_object_or_404(College, id=id)

    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm(instance=obj)  
    return render(request, 'modals/college_modal.html',{'form':form})


@login_required()
def college_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(College, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'college'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def graduate(request):
    if request.method == 'POST':
        form = GraduateForm(request.POST)
        if form.is_valid():
            graduate = form.save(commit=False)
            graduate.user_id = request.user.id
            graduate.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'graduate'})
    else:
        form = GraduateForm()  
    return render(request, 'modals/graduate_modal.html',{'form':form})

@login_required()
def graduate_edit(request, id):
    obj = get_object_or_404(Graduate, id=id)

    if request.method == 'POST':
        form = GraduateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'graduate'})
    else:
        form = GraduateForm(instance=obj)  
    return render(request, 'modals/graduate_modal.html',{'form':form})


@login_required()
def graduate_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Graduate, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'graduate'}) 
    else:
        return render(request, 'modals/delete_modal.html')
############################################################### END LOAD MODAL IN EDUCATION PAGE ######################################################################








############################################################### LOADED DATA IN ELIGIBILITY PAGE #########################################################################
@login_required()
def eligibility(request):
    return render(request, 'eligibility.html')

@login_required()
def eligibility_data(request):
    obj_eligibility = Eligibility.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/eligibility_data.html', {'obj_eligibility':obj_eligibility})

############################################################### END LOADED DATA IN ELIGIBILITY PAGE #########################################################################

############################################################### LOAD MODAL IN EDUCATION PAGE ######################################################################
@login_required()
def eligibility_add(request):
    if request.method == 'POST':
        form = EligibilityForm(request.POST)
        if form.is_valid():
            eligibility = form.save(commit=False)
            eligibility.user_id = request.user.id
            eligibility.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'eligibility'})
    else:
        form = EligibilityForm()  
    return render(request, 'modals/eligibility_modal.html',{'form':form})

@login_required()
def eligibility_edit(request, id):
    obj = get_object_or_404(Eligibility, id=id)

    if request.method == 'POST':
        form = EligibilityForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'eligibility'})
    else:
        form = EligibilityForm(instance=obj)  
    return render(request, 'modals/eligibility_modal.html',{'form':form})


@login_required()
def eligibility_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Eligibility, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'eligibility'}) 
    else:
        return render(request, 'modals/delete_modal.html')
############################################################### END LOAD MODAL IN EDUCATION PAGE ######################################################################








############################################################### LOADED DATA IN ELIGIBILITY PAGE #########################################################################
@login_required()
def documents(request):
    return render(request, 'documents.html')


@login_required()
def documents_data(request):
    obj_pds = get_or_none(PDS, user_id=request.user)
    obj_tor = get_or_none(TOR, user_id=request.user)
    obj_cav = get_or_none(CAV, user_id=request.user)
    obj_diploma = get_or_none(Diploma, user_id=request.user)
    obj_birthcert = get_or_none(BirthCert, user_id=request.user)
    obj_eligibilitydoc = get_or_none(EligibilityDoc, user_id=request.user)
    obj_marriagecert = get_or_none(MarriageCert, user_id=request.user)
    obj_sketch = get_or_none(Sketch, user_id=request.user)
    obj_waiver = get_or_none(Waiver, user_id=request.user)

    obj_barangay = get_or_none(Barangay, user_id=request.user)
    obj_nbi = get_or_none(NBI, user_id=request.user)
    obj_police = get_or_none(Police, user_id=request.user)
    obj_fiscal = get_or_none(Fiscal, user_id=request.user)
    obj_mtc = get_or_none(MTC, user_id=request.user)
    obj_rtc = get_or_none(RTC, user_id=request.user)
    obj_pnpdi = get_or_none(PNPDI, user_id=request.user)
    return render(request, 'loaded_data/documents_data.html',{
        'obj_pds':obj_pds,
        'obj_tor':obj_tor,
        'obj_cav':obj_cav,
        'obj_diploma':obj_diploma,
        'obj_birthcert':obj_birthcert,
        'obj_eligibilitydoc':obj_eligibilitydoc,
        'obj_marriagecert':obj_marriagecert,
        'obj_sketch':obj_sketch,
        'obj_waiver':obj_waiver,
        'obj_barangay':obj_barangay,
        'obj_nbi':obj_nbi,
        'obj_police':obj_police,
        'obj_fiscal':obj_fiscal,
        'obj_mtc':obj_mtc,
        'obj_rtc':obj_rtc,
        'obj_pnpdi':obj_pnpdi,
    })


@login_required()
def pds(request):
    try:
        obj = request.user.pds
    except ObjectDoesNotExist:
        obj = PDS(user=request.user)

    if request.method == 'POST':
        form = PDSForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = PDSForm(instance=obj)
    return render(request, 'modals/pds_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def pds_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(PDS, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def tor(request):
    try:
        obj = request.user.tor
    except ObjectDoesNotExist:
        obj = TOR(user=request.user)

    if request.method == 'POST':
        form = TORForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = TORForm(instance=obj)
    return render(request, 'modals/tor_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def tor_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(TOR, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def cav(request):
    try:
        obj = request.user.cav
    except ObjectDoesNotExist:
        obj = CAV(user=request.user)

    if request.method == 'POST':
        form = CAVForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = CAVForm(instance=obj)
    return render(request, 'modals/cav_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def cav_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(CAV, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def diploma(request):
    try:
        obj = request.user.diploma
    except ObjectDoesNotExist:
        obj = Diploma(user=request.user)

    if request.method == 'POST':
        form = DiplomaForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = DiplomaForm(instance=obj)
    return render(request, 'modals/diploma_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def diploma_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Diploma, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def birthcert(request):
    try:
        obj = request.user.birthcert
    except ObjectDoesNotExist:
        obj = BirthCert(user=request.user)

    if request.method == 'POST':
        form = BirthCertForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = BirthCertForm(instance=obj)
    return render(request, 'modals/birthcert_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def birthcert_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(BirthCert, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def eligibilitydoc(request):
    try:
        obj = request.user.eligibilitydoc
    except ObjectDoesNotExist:
        obj = EligibilityDoc(user=request.user)

    if request.method == 'POST':
        form = EligibilityDocForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = EligibilityDocForm(instance=obj)
    return render(request, 'modals/eligibilitydoc_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def eligibilitydoc_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(EligibilityDoc, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def marriagecert(request):
    try:
        obj = request.user.marriagecert
    except ObjectDoesNotExist:
        obj = MarriageCert(user=request.user)

    if request.method == 'POST':
        form = MarriageCertForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = MarriageCertForm(instance=obj)
    return render(request, 'modals/marriagecert_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def marriagecert_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(MarriageCert, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def sketch(request):
    try:
        obj = request.user.sketch
    except ObjectDoesNotExist:
        obj = Sketch(user=request.user)

    if request.method == 'POST':
        form = SketchForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = SketchForm(instance=obj)
    return render(request, 'modals/sketch_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def sketch_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Sketch, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def waiver(request):
    try:
        obj = request.user.waiver
    except ObjectDoesNotExist:
        obj = Waiver(user=request.user)

    if request.method == 'POST':
        form = WaiverForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = WaiverForm(instance=obj)
    return render(request, 'modals/waiver_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def waiver_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Waiver, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def barangay(request):
    try:
        obj = request.user.barangay
    except ObjectDoesNotExist:
        obj = Barangay(user=request.user)

    if request.method == 'POST':
        form = BarangayForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = BarangayForm(instance=obj)
    return render(request, 'modals/barangay_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def barangay_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Barangay, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def nbi(request):
    try:
        obj = request.user.nbi
    except ObjectDoesNotExist:
        obj = NBI(user=request.user)

    if request.method == 'POST':
        form = NBIForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = NBIForm(instance=obj)
    return render(request, 'modals/nbi_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def nbi_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(NBI, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def police(request):
    try:
        obj = request.user.police
    except ObjectDoesNotExist:
        obj = Police(user=request.user)

    if request.method == 'POST':
        form = PoliceForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = PoliceForm(instance=obj)
    return render(request, 'modals/police_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def police_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Police, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def fiscal(request):
    try:
        obj = request.user.fiscal
    except ObjectDoesNotExist:
        obj = Fiscal(user=request.user)

    if request.method == 'POST':
        form = FiscalForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = FiscalForm(instance=obj)
    return render(request, 'modals/fiscal_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def fiscal_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Fiscal, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def mtc(request):
    try:
        obj = request.user.mtc
    except ObjectDoesNotExist:
        obj = MTC(user=request.user)

    if request.method == 'POST':
        form = MTCForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = MTCForm(instance=obj)
    return render(request, 'modals/mtc_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def mtc_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(MTC, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def rtc(request):
    try:
        obj = request.user.rtc
    except ObjectDoesNotExist:
        obj = RTC(user=request.user)

    if request.method == 'POST':
        form = RTCForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = RTCForm(instance=obj)
    return render(request, 'modals/rtc_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def rtc_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(RTC, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def pnpdi(request):
    try:
        obj = request.user.pnpdi
    except ObjectDoesNotExist:
        obj = PNPDI(user=request.user)

    if request.method == 'POST':
        form = PNPDIForm(request.POST, request.FILES ,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'documents'})
    else:
        form = PNPDIForm(instance=obj)
    return render(request, 'modals/pnpdi_modal.html',{
        'form':form,
        'obj':obj,
    })

@login_required()
def pnpdi_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(PNPDI, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'documents'}) 
    else:
        return render(request, 'modals/delete_modal.html')