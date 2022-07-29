from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    return render(request, 'home.html',)

@login_required()
def personal_info(request):
    return render(request, 'includes/personal_info_modal.html',)