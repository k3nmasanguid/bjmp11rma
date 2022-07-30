from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from rma.models import PersonalInfo
from rma.forms import PersonalInfoForm
def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None

@login_required()
def home(request):
    obj_pinfo = get_or_none(PersonalInfo, user_id=request.user)
    context = {
        'obj_pinfo': obj_pinfo,
    }
    return render(request, 'home.html',context)

@login_required()
def personal_info(request):
    obj_pinfo = get_or_none(PersonalInfo, user_id=request.user)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, instance=obj_pinfo)
        if form.is_valid():
            form.save()
    else:
        form = PersonalInfoForm(instance=obj_pinfo)
    return render(request, 'includes/personal_info_modal.html',{'form':form})