
import json
from wsgiref.headers import Headers
from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rma.models import PermanentAddress, PersonalInfo, PresentAddress, Spouse, Father, Mother
from rma.forms import PersonalInfoForm, PresentAddressForm, PermanentAddressForm, SpouseForm, FatherForm, MotherForm

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