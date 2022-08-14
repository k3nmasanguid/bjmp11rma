
from django.shortcuts import render
from authentication.models import User
from rma.models import College, Quota
from django.db.models import Q
def bjmpadmin(request):
    batches = Quota.objects.all().order_by('-id')
    queryset1  = User.objects.prefetch_related('batch').filter(batch__batch='2023-01')
    
    infos = User.objects.filter(id__in=queryset1).select_related('personalinfo')
    total_applicant = infos.count()
    male_applicant = infos.filter(personalinfo__gender__iexact='MALE').count()
    female_applicant = infos.filter(personalinfo__gender__iexact='FEMALE').count()
    crim_course = College.objects.filter(Q(user_id__in=queryset1) & ~Q(year_graduated__iexact="N/A") & Q(course__icontains="criminology")).count()
    
    context = {
        'batches':batches,
        'infos':infos,
        'total_applicant':total_applicant,
        'male_applicant':male_applicant,
        'female_applicant':female_applicant,
        'crim_course':crim_course,
    }
  
    return render(request, 'bjmpadmin/bjmpadmin.html',context)#{'results':results,})