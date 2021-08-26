from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect
import json

# Create your views here.
def Home(request):
    return render(request, 'E_Form_app/home.html')

def previewform(request):
    return render(request, 'E_Form_app/preview_Form.html')

def createformdata(request):
    if request.method=="POST":
        Qsns = request.POST.get('Qsns', '')
        data  = json.loads(Qsns)
        print(data)

        return HttpResponse("m")




def createform(request):
    if(request.user.is_authenticated):
        return render(request, 'E_Form_app/createform.html')
    else:
        # return redirect("Home")
        return render(request, 'E_Form_app/createform.html')





def hlogout(request):
    
    logout(request)
    return redirect('Home')
    
