
from ast import Await
from ctypes import Union
from django.shortcuts import render, redirect, HttpResponse
from authentication.models import User
from rma.models import Quota,PersonalInfo, PresentAddress, PermanentAddress, Spouse, Children, Father, Mother, Sibling, Primary, HighSchool,SeniorHigh, College, Graduate, Eligibility
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
                total_applicant = infos.count()
                male_applicant = infos.filter(personalinfo__gender__iexact='MALE').count()
                female_applicant = infos.filter(personalinfo__gender__iexact='FEMALE').count()
                crim_course = College.objects.filter(Q(user_id__in=queryset1) & ~Q(year_graduated__iexact="N/A") & Q(course__icontains="criminology")).count()
                
                context = {
                    'college':college,
                    'selected_batch':selected_batch,
                    'batches':batches,
                    'infos':infos,
                    'total_applicant':total_applicant,
                    'male_applicant':male_applicant,
                    'female_applicant':female_applicant,
                    'crim_course':crim_course,
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
    }
    return render(request,'bjmpadmin/bjmpadmin_profile.html',context)