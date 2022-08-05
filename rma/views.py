

from django.shortcuts import get_object_or_404, render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rma.models import Graduate, PermanentAddress, PersonalInfo, PresentAddress, Spouse, Father, Mother, Sibling, Children, Primary, HighSchool, SeniorHigh, College, Graduate, Eligibility
from rma.forms import PersonalInfoForm, PresentAddressForm, PermanentAddressForm, SpouseForm, FatherForm, MotherForm, SiblingForm, ChildrenForm, PrimaryForm, HighSchoolForm, SeniorHighForm, CollegeForm, GraduateForm, EligibilityForm

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


############################################################### LOADED DATA IN BACKGROUND PAGE #########################################################################

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
def sibling_data(request):
    obj_sibling = Sibling.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/sibling_data.html',{'obj_sibling':obj_sibling})


@login_required()
def children_data(request):
    obj_children = Children.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/children_data.html',{'obj_children':obj_children})

############################################################### END LOADED DATA IN BACKGROUND PAGE #########################################################################

###############################################################  LOAD MODAL IN BACKGROUND PAGE ######################################################################

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

@login_required()
def sibling(request):
    if request.method == 'POST':
        form = SiblingForm(request.POST)
        if form.is_valid():
            sibling = form.save(commit=False)
            sibling.user_id = request.user.id
            sibling.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'sibling'})
    else:
        form = SiblingForm()  
    return render(request, 'modals/sibling_modal.html',{'form':form})

@login_required()
def sibling_edit(request, id):
    obj = get_object_or_404(Sibling, id=id)

    if request.method == 'POST':
        form = SiblingForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'sibling'})
    else:
        form = SiblingForm(instance=obj)  
    return render(request, 'modals/sibling_modal.html',{'form':form})


@login_required()
def sibling_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Sibling, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'sibling'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def children(request):
    if request.method == 'POST':
        form = ChildrenForm(request.POST)
        if form.is_valid():
            children = form.save(commit=False)
            children.user_id = request.user.id
            children.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'children'})
    else:
        form = ChildrenForm()  
    return render(request, 'modals/children_modal.html',{'form':form})

@login_required()
def children_edit(request, id):
    obj = get_object_or_404(Children, id=id)

    if request.method == 'POST':
        form = ChildrenForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'children'})
    else:
        form = ChildrenForm(instance=obj)  
    return render(request, 'modals/children_modal.html',{'form':form})


@login_required()
def children_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Children, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'children'}) 
    else:
        return render(request, 'modals/delete_modal.html')

###############################################################  END LOAD MODAL IN BACKGROUND PAGE ######################################################################


############################################################### LOADED DATA IN EDUCATION PAGE #########################################################################

@login_required()
def education(request):
    return render(request, 'education.html')

@login_required()
def primary_data(request):
    obj_primary = Primary.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/primary_data.html', {'obj_primary':obj_primary})

@login_required()
def high_school_data(request):
    obj_high_school = HighSchool.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/high_school_data.html', {'obj_high_school':obj_high_school})

@login_required()
def senior_high_data(request):
    obj_senior_high = SeniorHigh.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/senior_high_data.html', {'obj_senior_high':obj_senior_high})

@login_required()
def college_data(request):
    obj_college = College.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/college_data.html', {'obj_college':obj_college})

@login_required()
def graduate_data(request):
    obj_graduate = Graduate.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/graduate_data.html', {'obj_graduate':obj_graduate})

############################################################### END LOADED DATA IN EDUCATION PAGE #########################################################################


############################################################### LOAD MODAL IN EDUCATION PAGE ######################################################################
@login_required()
def primary(request):
    if request.method == 'POST':
        form = PrimaryForm(request.POST)
        if form.is_valid():
            primary = form.save(commit=False)
            primary.user_id = request.user.id
            primary.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'primary'})
    else:
        form = PrimaryForm()  
    return render(request, 'modals/primary_modal.html',{'form':form})

@login_required()
def primary_edit(request, id):
    obj = get_object_or_404(Primary, id=id)

    if request.method == 'POST':
        form = PrimaryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'primary'})
    else:
        form = PrimaryForm(instance=obj)  
    return render(request, 'modals/primary_modal.html',{'form':form})


@login_required()
def primary_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Primary, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'primary'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def high_school(request):
    if request.method == 'POST':
        form = HighSchoolForm(request.POST)
        if form.is_valid():
            high_school = form.save(commit=False)
            high_school.user_id = request.user.id
            high_school.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'high_school'})
    else:
        form = HighSchoolForm()  
    return render(request, 'modals/high_school_modal.html',{'form':form})

@login_required()
def high_school_edit(request, id):
    obj = get_object_or_404(HighSchool, id=id)

    if request.method == 'POST':
        form = HighSchoolForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'high_school'})
    else:
        form = HighSchoolForm(instance=obj)  
    return render(request, 'modals/high_school_modal.html',{'form':form})


@login_required()
def high_school_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(HighSchool, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'high_school'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def senior_high(request):
    if request.method == 'POST':
        form = SeniorHighForm(request.POST)
        if form.is_valid():
            senior_high = form.save(commit=False)
            senior_high.user_id = request.user.id
            senior_high.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'senior_high'})
    else:
        form = SeniorHighForm()  
    return render(request, 'modals/senior_high_modal.html',{'form':form})

@login_required()
def senior_high_edit(request, id):
    obj = get_object_or_404(SeniorHigh, id=id)

    if request.method == 'POST':
        form = SeniorHighForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'senior_high'})
    else:
        form = SeniorHighForm(instance=obj)  
    return render(request, 'modals/senior_high_modal.html',{'form':form})


@login_required()
def senior_high_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(SeniorHigh, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'senior_high'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.save(commit=False)
            college.user_id = request.user.id
            college.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm()  
    return render(request, 'modals/college_modal.html',{'form':form})

@login_required()
def college_edit(request, id):
    obj = get_object_or_404(College, id=id)

    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm(instance=obj)  
    return render(request, 'modals/college_modal.html',{'form':form})


@login_required()
def college_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(College, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'college'}) 
    else:
        return render(request, 'modals/delete_modal.html')


@login_required()
def college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.save(commit=False)
            college.user_id = request.user.id
            college.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm()  
    return render(request, 'modals/college_modal.html',{'form':form})

@login_required()
def college_edit(request, id):
    obj = get_object_or_404(College, id=id)

    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'college'})
    else:
        form = CollegeForm(instance=obj)  
    return render(request, 'modals/college_modal.html',{'form':form})


@login_required()
def college_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(College, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'college'}) 
    else:
        return render(request, 'modals/delete_modal.html')

@login_required()
def graduate(request):
    if request.method == 'POST':
        form = GraduateForm(request.POST)
        if form.is_valid():
            graduate = form.save(commit=False)
            graduate.user_id = request.user.id
            graduate.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'graduate'})
    else:
        form = GraduateForm()  
    return render(request, 'modals/graduate_modal.html',{'form':form})

@login_required()
def graduate_edit(request, id):
    obj = get_object_or_404(Graduate, id=id)

    if request.method == 'POST':
        form = GraduateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'graduate'})
    else:
        form = GraduateForm(instance=obj)  
    return render(request, 'modals/graduate_modal.html',{'form':form})


@login_required()
def graduate_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Graduate, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'graduate'}) 
    else:
        return render(request, 'modals/delete_modal.html')
############################################################### END LOAD MODAL IN EDUCATION PAGE ######################################################################








############################################################### LOADED DATA IN ELIGIBILITY PAGE #########################################################################
@login_required()
def eligibility(request):
    return render(request, 'eligibility.html')

@login_required()
def eligibility_data(request):
    obj_eligibility = Eligibility.objects.filter(user_id=request.user)
    return render(request, 'loaded_data/eligibility_data.html', {'obj_eligibility':obj_eligibility})

############################################################### END LOADED DATA IN ELIGIBILITY PAGE #########################################################################

############################################################### LOAD MODAL IN EDUCATION PAGE ######################################################################
@login_required()
def eligibility_add(request):
    if request.method == 'POST':
        form = EligibilityForm(request.POST)
        if form.is_valid():
            eligibility = form.save(commit=False)
            eligibility.user_id = request.user.id
            eligibility.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'eligibility'})
    else:
        form = EligibilityForm()  
    return render(request, 'modals/eligibility_modal.html',{'form':form})

@login_required()
def eligibility_edit(request, id):
    obj = get_object_or_404(Eligibility, id=id)

    if request.method == 'POST':
        form = EligibilityForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'eligibility'})
    else:
        form = EligibilityForm(instance=obj)  
    return render(request, 'modals/eligibility_modal.html',{'form':form})


@login_required()
def eligibility_delete(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Eligibility, id=id)
        obj.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'eligibility'}) 
    else:
        return render(request, 'modals/delete_modal.html')
############################################################### END LOAD MODAL IN EDUCATION PAGE ######################################################################








############################################################### LOADED DATA IN ELIGIBILITY PAGE #########################################################################
@login_required()
def documents(request):
    return render(request, 'documents.html')


@login_required()
def documents_data(request):
    return render(request, 'loaded_data/documents_data.html')