from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def Home(request):
    return render(request, 'E_Form_app/home.html')


def createform(request):
    if(request.user.is_authenticated):
        return render(request, 'E_Form_app/createform.html')
    else:
        # return redirect("Home")
        return render(request, 'E_Form_app/createform.html')





def hlogout(request):
    
    logout(request)
    return redirect('Home')
    
