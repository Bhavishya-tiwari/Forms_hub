from django import http
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse, redirect
import json
import datetime 
from datetime import date, datetime
from django.contrib import messages
from .models import Forms

from django.utils import timezone
import pytz    

# Create your views here.
# Forms.objects.all().delete()
# Res.objects.all().delete()


def v(s):
    if s != "":
        return True
    else:
        return False
def g(d):
    return int(d)    
def aa(s, d):
    return list(str(s).split(d)) 


def Home(request):

    return render(request, 'E_Form_app/home.html')





def createformdata(request):
    if request.method == "POST":
        try:

            Qsns = request.POST.get('Qsns', '')

            data = json.loads(Qsns)
            q = data["Qsns"]
            # j = json.dumps(q)
            # s = q.toString()
            s = ''
            for qs in q:
                e = str(qs["Qno"])
                qs["Qno"] = e

                if qs["Type"] == "MultipleC" or qs["Type"] == "SingleC":
                    opt_S = ''
                    for opt in qs["opt"]:
                        opt_S = opt_S + opt + '&'
                    qs["opt"] = opt_S

                    s = s + str(qs) + '$'

                else:
                    s = s+str(qs) + '$'

            fm = Forms(Form_Title=data['Title'], Disc=data["Disc"], Admin_Name=request.user.first_name + request.user.last_name, Admin_Email=request.user.email,
                       Admin_Username=request.user.username,
                       Timestamp_Created=datetime.now(), sd=data["sd"], st=data["st"],  cd=data["cd"], ct=data["ct"],form_type = data["Type"],
                       Qsns=s,
                       )
            fm.save()

            # rs = Res(idd = fm.fno )
            # rs.save()
            sno = str(fm.fno)
            # lik = "http://127.0.0.1:8000/"+"FormHub/" + request.user.username + "/" + sno
            lik ="FormHub/" + request.user.username + "/" + sno
            
            return HttpResponse(lik)
        except:
            return HttpResponse("jj")
            
            


def fillform(request, admin, id):
    try:
            
        post = Forms.objects.filter(fno=id).first()
        
        if post.Admin_Username == admin:
            tz_NY = pytz.timezone('Asia/Kolkata')   
            datetime_NY = datetime.now(tz_NY)  
            d =  datetime_NY.strftime("%Y-%m-%d")    
            t =  datetime_NY.strftime("%H:%M:%S.%f")    
          
         

            
            tim = list(str(t).split(":"))
            # dat = list(str(date.today().strftime("%d/%m/%Y")).split("/"))
            dat = list(str(d).split("-"))
            tod = datetime(g(dat[0]), g(dat[1]), g(dat[2]),g(tim[0]), g(tim[1]),11)

            sd = aa( post.sd,"-")
            st = aa(post.st, ":")
            cd = aa( post.cd,"-")
            ct = aa(post.ct, ":")

            sta = datetime(g(sd[0]),g(sd[1]),g(sd[2]),g(st[0]), g(st[1]), 11)
            end = datetime(g(cd[0]),g(cd[1]),g(cd[2]),g(ct[0]), g(ct[1]), 11)
            perm = "allowed"
            tosend=[]
            st = post.Responses
            re = aa(st, "%")[:-1]
            for r in re:
                a = aa(r, "#")[:-1]
                e = json.loads(str(a[-1]).replace("'", '"'))
                
                if post.form_type == "S":
                    if e["username"] == request.user.username:
                        perm = "not"
                    return render(request, 'E_Form_app/late.html', {"o":"already"})


                    
                    

                

            

         
            if ((tod < end) and (tod > sta) and (perm == "allowed" )) or (request.user.username == post.Admin_Username) :
                
            

                p = post.Qsns
                q = list(p.split("$"))[:-1]
                qsns = []
                for qs in q:
                    r = qs.replace("'", '"')
                    l = json.loads(r)
                    qsns.append(l)

                    if l["Type"] == "MultipleC" or l["Type"] == "SingleC":
                        ll = list(l["opt"].split('&'))[:-1]
                        l["opt"] = ll

                o = {
                    "An": post.Admin_Name,
                    "Ae": post.Admin_Email,
                    "T": post.Form_Title,
                    "D": post.Disc,
                    "sd": post.sd,
                    "st": post.st,
                    "cd": post.cd,
                    "ct": post.ct,
                    "Q": qsns,
                    "id": id
                }
                return render(request, 'E_Form_app/filllform.html', {"Qs": o})
            else:
                o ={
                    "E":"opps" , "st":sta, "end":end, "t":tod, "e":tod>sta, "l":tod<end, "t2":tim, "T1":tim[1], "j":g(tim[1])
                }
                return render(request, 'E_Form_app/late.html', {"o":o})
        else:
            messages.error(request, "Errorr")
            return redirect("Home")
    except:
        messages.error(request, "Error")
        return redirect("Home")
            


def createform(request):
    if(request.user.is_authenticated):
        return render(request, 'E_Form_app/createform.html')
    else:

        messages.error(request, "Please login to create")
        return redirect("/")






def myforms(request):
    u = request.user.username
    post = Forms.objects.filter(Admin_Username=u).all()
    o = []
    for p in post:
        oo = {
            "T":p.Form_Title,
            "D":p.Disc,
          
            "id":p.fno,
        }
        o.append(oo)
    return render(request, 'E_Form_app/myforms.html',{"f":o})
    
            







def viewmyforms(request, fid):
    post = Forms.objects.filter(fno=fid).first()
    if request.user.username == post.Admin_Username:
        # lik = "http://127.0.0.1:8000/"+"FormHub/" + request.user.username + "/" + str(fid)
        lik = "https://form-hub.herokuapp.com/"+"FormHub/" + request.user.username + "/" + str(fid)
        st = post.Responses
        re = aa(st, "%")[:-1]
        tosend=[]
        p = post.Qsns
        q = list(p.split("$"))[:-1]
        qsns = []
        for qs in q:
            r = qs.replace("'", '"')
            l = json.loads(r)
            qsns.append(l)

            if l["Type"] == "MultipleC" or l["Type"] == "SingleC":
                ll = list(l["opt"].split('&'))[:-1]
                l["opt"] = ll

        
        for r in re:
            a = aa(r, "#")[:-1]
            e = json.loads(str(a[-1]).replace("'", '"'))
            o = {
                "P":e,
                "r":[]
            }

            for r in a[:-1]:
                f = str(r).replace("'", '"')

                js = json.loads(f)
                if js["T"] == "M":
                    js["A"]=str(js["A"]).replace("!",",")[:-1]

                o["r"].append(js)      
            tosend.append(o)
        if post.form_type == "M":
                z ="Multiple submits from one person" 
        else:
                z = "Single submit from one person"

             
        ps = {
                "S":post.sd + " "+ post.st,
                "C":post.cd + " "+ post.ct,
                "T":post.Form_Title,
                "Ty":z,
                "i":post.fno,
            }
            
                
        return render(request, 'E_Form_app/viewmyforms.html',{"dt":tosend, "lk":lik, "q":qsns, "p":ps})
        


        

    



def changesettings(request, upd):
    post = Forms.objects.filter(fno=upd).first()
    if request.method == "POST":
        if request.user.username == post.Admin_Username:
            d = request.POST.get('dat')
            t = request.POST.get('tim')
            ty = request.POST.get('typee')

            if(t != "" and d != ""):

                post.cd = str(d)
                post.ct = str(t)

            
            if(ty == "on"):
                post.form_type = "M"
            else:
                post.form_type = "S"
            post.save()
    messages.success(request, "Form settings updated")
    return redirect('/viewmyforms'+str(upd))

def deleteform(request, df):
    post = Forms.objects.filter(fno=df).first()
    if request.method == "POST":
        if request.user.username == post.Admin_Username:
            post.delete()
            messages.success(request, "Form deleted sucsessfully")
            return redirect('/myforms')





        

    

def givedata(request, ii):
    if(request.user.is_authenticated):

        post = Forms.objects.filter(fno=ii).first()
        p = post.Qsns
        q = list(p.split("$"))[:-1]
        qsns = []
        for qs in q:
            r = qs.replace("'", '"')
            l = json.loads(r)
            qsns.append(l)

            if l["Type"] == "MultipleC" or l["Type"] == "SingleC":
                ll = list(l["opt"].split('&'))[:-1]
                l["opt"] = ll

        o = {
            "An": post.Admin_Name,
            "Ae": post.Admin_Email,
            "T": post.Form_Title,
            "D": post.Disc,
            "sd": post.sd,
            "st": post.st,
            "cd": post.cd,
            "ct": post.ct,
            "Q": qsns,
            "Qr": p,
            "id": ii,
        }
        return HttpResponse(json.dumps(o))
    else:
        return HttpResponse("err")


def saveresponse(request, res):
    if request.method == "POST":
        if(request.user.is_authenticated):
            post = Forms.objects.filter(fno=res).first()

            # tim = list(str(datetime.now().strftime("%H:%M:%S")).split(":"))
            # dat = list(str(date.today().strftime("%d/%m/%Y")).split("/"))
            # tod = datetime(g(dat[2]), g(dat[1]), g(dat[0]),int(tim[0]), int(tim[1]),int(tim[2]))

            # sd = aa( post.sd,"-")
            # st = aa(post.st, ":")
            # cd = aa( post.cd,"-")
            # ct = aa(post.ct, ":")

            # sta = datetime(g(sd[0]),g(sd[1]),g(sd[2]),g(st[0]), g(st[1]), 11)
            # end = datetime(g(cd[0]),g(cd[1]),g(cd[2]),g(ct[0]), g(ct[1]), 11)

            # if tod < end and tod > sta :
            tz_NY = pytz.timezone('Asia/Kolkata')   
            datetime_NY = datetime.now(tz_NY)  
            d =  datetime_NY.strftime("%Y-%m-%d")    
            t =  datetime_NY.strftime("%H:%M:%S.%f")    
          
         

            
            tim = list(str(t).split(":"))
            # dat = list(str(date.today().strftime("%d/%m/%Y")).split("/"))
            dat = list(str(d).split("-"))
            tod = datetime(g(dat[0]), g(dat[1]), g(dat[2]),g(tim[0]), g(tim[1]),11)

            sd = aa( post.sd,"-")
            st = aa(post.st, ":")
            cd = aa( post.cd,"-")
            ct = aa(post.ct, ":")

            sta = datetime(g(sd[0]),g(sd[1]),g(sd[2]),g(st[0]), g(st[1]), 11)
            end = datetime(g(cd[0]),g(cd[1]),g(cd[2]),g(ct[0]), g(ct[1]), 11)
            perm = "allowed"
            tosend=[]
            st = post.Responses
            re = aa(st, "%")[:-1]
            for r in re:
                a = aa(r, "#")[:-1]
                e = json.loads(str(a[-1]).replace("'", '"'))
                
                if post.form_type == "S":
                    if e["username"] == request.user.username:
                        perm = "not"
         
            if ((tod < end) and (tod > sta) and (perm == "allowed" )) or (request.user.username == post.Admin_Username):




                prv = post.Responses
                A = request.POST.get('Aa', '')
                r = ''
                A = json.loads(A)
                for a in A["A"]:
                    if a["T"] == "M":
                        As = ''
                        for o in a["A"]:
                            As = As + str(o)+"!"
                        a["A"] = As
                        r = r + str(a) + "#"

                    else:
                        r = r + str(a) + '#'
                
                d = {
                    "name": request.user.first_name + " " + request.user.last_name,
                    "username": request.user.username,
                    "email": request.user.email,
                    "time": str(tod),
                }
                r = r + str(d)+'#'
                post.Responses = post.Responses + r + "%"
                # post.Responses = ""

                post.save()
                return HttpResponse("done")
            else:
                return HttpResponse("LorE")
def submitted(req):
    
    return render ( req, 'E_Form_app/late.html', {"o":"fir"})
    



def hlogout(request):
    logout(request)
    messages.error(request, "Logged out sucsessfully")
    return redirect('Home')

