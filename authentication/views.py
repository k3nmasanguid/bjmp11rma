import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from authentication.forms import UserForm
from verify_email.email_handler import send_verification_email



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                inactive_user = send_verification_email(request, form)
                
                return HttpResponse(status=200, headers={'HX-Trigger': json.dumps({
                            "showMessage": f"Please verify your email. We sent an email to {inactive_user.email}"
                        })
                    })
        else:
            form = UserForm()
        return render(request,'modals/register_modal.html', {'form':form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        message = ''
        if request.method == 'POST':
            user = authenticate(
                email = request.POST.get('email'),
                password = request.POST.get('password'),
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Invalid email or password - Try again'

        return render(request,'login.html', {'message':message})

def logout_user(request):
    logout(request)
    return redirect('login')

