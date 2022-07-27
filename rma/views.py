from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    return render(request, 'home.html',)