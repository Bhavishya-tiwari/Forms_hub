from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'E_Form_app/home.html')

def createform(request):
    return render(request, 'E_Form_app/home.html')
