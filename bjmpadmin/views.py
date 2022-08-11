from django.shortcuts import render
from authentication.models import User

def bjmpadmin(request):
    w = User.objects.prefetch_related('batch').filter(batch__batch='2022-01')

    
    
    return render(request, 'bjmpadmin/bjmpadmin.html',)