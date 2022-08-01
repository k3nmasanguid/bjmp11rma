
import json
from wsgiref.headers import Headers
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rma.models import PersonalInfo, PresentAddress
from rma.forms import PersonalInfoForm, PresentAddressForm

def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None

@login_required()
def home(request):
    return render(request, 'home.html')

############################################################### LOADED DATA #########################################################################
@login_required()  
def personal_info_data(request):
    obj_pinfo = get_or_none(PersonalInfo, user_id=request.user)
    return render(request, 'loaded_data/personal_info_data.html',{'obj_pinfo':obj_pinfo})

@login_required()
def present_address_data(request):
    obj_present_address = get_or_none(PresentAddress, user_id=request.user)
    return render(request, 'loaded_data/present_address_data.html',{'obj_present_address':obj_present_address})

############################################################### END LOADED DATA ######################################################################
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
            print('FAILED')
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
            return HttpResponse(status=204, headers={'HX-Trigger': ''})
        else:
            print('FAILED')
    else:
        form = PresentAddressForm(instance=obj)  
    return render(request, 'modals/present_address_modal.html',{'form':form})