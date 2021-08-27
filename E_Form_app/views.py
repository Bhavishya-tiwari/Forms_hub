from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect
import json
from datetime import datetime
from .models import Forms,Res
# Create your views here.
# Forms.objects.all().delete()
# Res.objects.all().delete()



def Home(request):
    return render(request, 'E_Form_app/home.html')


def previewform(request):
    if request.method=="POST":
        return render(request, 'E_Form_app/preview_Form.html')




def createformdata(request):
    if request.method=="POST":
        try:

            Qsns = request.POST.get('Qsns', '')
           
            
            data  = json.loads(Qsns)
            q = data["Qsns"]
            # j = json.dumps(q)
            # s = q.toString()
            s = ''
            print(type(q))
            for qs in q:
                e = str(qs["Qno"])
                qs["Qno"] = e

                if qs["Type"] == "MultipleC" or qs["Type"] =="SingleC":
                    opt_S=''
                    for opt in qs["opt"]:
                        opt_S =opt_S + opt + '&'
                    print(opt_S[:-1]) 
                    qs["opt"] = opt_S

                    s = s + str(qs) + '$'

                

                else:
                    s=s+str(qs) + '$'
                    
            print(s)





            fm = Forms(Form_Title=data['Title'],Disc = data["Disc"] ,Admin_Name = request.user.first_name + request.user.last_name,Admin_Email = request.user.email ,
            Admin_Username=request.user.username,
            Timestamp_Created = datetime.now(), sd =data["sd"], st=data["st"],  cd=data["cd"], ct=data["ct"],
            Qsns = s, 
              )
            fm.save()
            
            rs = Res(idd = fm.fno )
            rs.save()
            sno = str(fm.fno) 
            lik = "http://127.0.0.1:8000/"+"FormHub/" +  request.user.username +"/" +sno  
            return HttpResponse(lik)
        except:
            print("F")
            return HttpResponse("jj")

            







        
def fillform(request,admin,id):
    post = Forms.objects.filter(fno=id).first()
    p =post.Qsns
    q=list(p.split("$"))[:-1]
    qsns = []
    for qs in q:
        r = qs.replace("'", '"')
        l = json.loads(r)
        qsns.append(l)

        if l["Type"] =="MultipleC" or l["Type"] =="SingleC":
            ll =list( l["opt"].split('&'))[:-1]
            l["opt"] = ll

            

    # print(qsns)
    o = {
        "An":post.Admin_Name,
        "Ae":post.Admin_Email,
        "T":post.Form_Title,
        "D":post.Disc,
        "sd":post.sd,
        "st":post.st,
        "cd":post.cd,
        "ct":post.ct,
        "Q":qsns,
        "id":id
        

    }
    

    


    return render(request, 'E_Form_app/filllform.html', {"Qs":o})






def createform(request):
    if(request.user.is_authenticated):
        return render(request, 'E_Form_app/createform.html')
    else:
        # return redirect("Home")
        return render(request, 'E_Form_app/createform.html')



def givedata(request, ii):
    post = Forms.objects.filter(fno=ii).first()
    p =post.Qsns
    q=list(p.split("$"))[:-1]
    qsns = []
    for qs in q:
        r = qs.replace("'", '"')
        l = json.loads(r)
        qsns.append(l)

        if l["Type"] =="MultipleC" or l["Type"] =="SingleC":
            ll =list( l["opt"].split('&'))[:-1]
            l["opt"] = ll
    

    o = {
        "An":post.Admin_Name,
        "Ae":post.Admin_Email,
        "T":post.Form_Title,
        "D":post.Disc,
        "sd":post.sd,
        "st":post.st,
        "cd":post.cd,
        "ct":post.ct,
        "Q":qsns,
        
        

    }
    return HttpResponse(json.dumps(o))

def hlogout(request):
    
    logout(request)
    return redirect('Home')
    
