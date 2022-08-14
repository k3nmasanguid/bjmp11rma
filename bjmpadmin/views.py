
from django.shortcuts import render
from authentication.models import User
from rma.models import College
from django.db.models import Q
def bjmpadmin(request):
    queryset1  = User.objects.prefetch_related('batch').filter(batch__batch='2024-01')
    # results = User.objects.filter(id__in=queryset1).select_related('personalinfo')
    # resultsss = College.objects.filter(user_id=2).select_related('user')
    infos = User.objects.filter(id__in=queryset1).select_related('personalinfo')
    


    context = {
        'infos':infos,
       
    }
    # college_results = College.objects.select_related('user')#.filter(Q(user_id__id=queryset1)& ~Q(year_graduated = 'N/A')).first()
    # # # for x in results:
    # # #     print(x.personalinfo.last_name,x.presentaddress.zip_code)
    # # # queryset2 = User.objects.filter(id=queryset1.id)
    # # # for x in queryset1 :
    # # #     print(x.id)
    # for x in queryset1:
    #     courses = College.objects.filter(user_id=x.id).select_related('user')
   

    return render(request, 'bjmpadmin/bjmpadmin.html',context)#{'results':results,})