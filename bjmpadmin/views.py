from django.shortcuts import render


def bjmpadmin(request):
    return render(request, 'bjmpadmin/bjmpadmin.html')