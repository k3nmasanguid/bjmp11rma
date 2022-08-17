
from ast import Await
from ctypes import Union
from tkinter import X
from django.shortcuts import render, redirect, HttpResponse
from authentication.models import User
from rma.models import Quota,PersonalInfo, PresentAddress, PermanentAddress, Spouse, Children, Father, Mother, Sibling, Primary, HighSchool,SeniorHigh, College, Graduate, Eligibility
from upload_docs.models import *
from django.db.models import Q
from rma.views import get_or_none


def bjmpadmin(request):
    if request.user.is_staff:
        batches = Quota.objects.all().order_by('-id')    
        return render(request, 'bjmpadmin/bjmpadmin.html',{'batches':batches})
    else:
        return redirect('home')
    

def bjmpadmin_search(request):
    
    if request.user.is_staff:
        batches = Quota.objects.all().order_by('-id')
        if request.method == 'GET':
            selected_batch = request.GET.get('batch')
            if selected_batch is None:
                return redirect('bjmpadmin')
            else:
                queryset1  = User.objects.prefetch_related('batch').filter(batch__batch=selected_batch)
                infos = User.objects.filter(id__in=queryset1).select_related('personalinfo')
                college = College.objects.filter(Q(user_id__in=queryset1) & ~Q(year_graduated='N/A'))
                eligibility = Eligibility.objects.filter(user_id__in=queryset1)
                total_applicant = infos.count()
                male_applicant = infos.filter(personalinfo__gender__iexact='MALE').count()
                female_applicant = infos.filter(personalinfo__gender__iexact='FEMALE').count()
                context = {
                    'college':college,
                    'eligibility':eligibility,
                    'selected_batch':selected_batch,
                    'batches':batches,
                    'infos':infos,
                    'total_applicant':total_applicant,
                    'male_applicant':male_applicant,
                    'female_applicant':female_applicant,
                }
        
                return render(request, 'bjmpadmin/bjmpadmin.html',context)
    else:
        return redirect('home')

def bjmpadmin_profile(request, id):
    obj_pinfo = get_or_none(PersonalInfo,user_id=id)
    obj_present_address = get_or_none(PresentAddress,user_id=id)
    obj_permanent_address = get_or_none(PermanentAddress, user_id=id)
    obj_spouse = get_or_none(Spouse, user_id=id)
    obj_children = Children.objects.filter(user_id=id)
    obj_father = get_or_none(Father, user_id=id)
    obj_mother = get_or_none(Mother, user_id=id)
    obj_sibling = get_or_none(Sibling, user_id=id)
    obj_primary = Primary.objects.filter(user_id=id)
    obj_high_school = HighSchool.objects.filter(user_id=id)
    obj_senior_high = SeniorHigh.objects.filter(user_id=id)
    obj_college = College.objects.filter(user_id=id)
    obj_graduate = Graduate.objects.filter(user_id=id)
    obj_eligibility = Eligibility.objects.filter(user_id=id)
    

    obj_pds = get_or_none(PDS, user_id=id)
    obj_tor = get_or_none(TOR, user_id=id)
    obj_cav = get_or_none(CAV, user_id=id)
    obj_diploma = get_or_none(Diploma, user_id=id)
    obj_birthcert = get_or_none(BirthCert, user_id=id)
    obj_eligibilitydoc = get_or_none(EligibilityDoc, user_id=id)
    obj_marriagecert = get_or_none(MarriageCert, user_id=id)
    obj_sketch = get_or_none(Sketch, user_id=id)
    obj_waiver = get_or_none(Waiver, user_id=id)

    obj_barangay = get_or_none(Barangay, user_id=id)
    obj_nbi = get_or_none(NBI, user_id=id)
    obj_police = get_or_none(Police, user_id=id)
    obj_fiscal = get_or_none(Fiscal, user_id=id)
    obj_mtc = get_or_none(MTC, user_id=id)
    obj_rtc = get_or_none(RTC, user_id=id)
    obj_pnpdi = get_or_none(PNPDI, user_id=id)
   
    context = {
        'obj_pinfo':obj_pinfo,
        'obj_present_address':obj_present_address,
        'obj_permanent_address':obj_permanent_address,
        'obj_spouse':obj_spouse,
        'obj_children':obj_children,
        'obj_father':obj_father,
        'obj_mother':obj_mother,
        'obj_sibling':obj_sibling,
        'obj_primary':obj_primary,
        'obj_high_school':obj_high_school,
        'obj_senior_high':obj_senior_high,
        'obj_college':obj_college,
        'obj_graduate':obj_graduate,
        'obj_eligibility':obj_eligibility,
        

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
    }
    return render(request,'bjmpadmin/bjmpadmin_profile.html',context)