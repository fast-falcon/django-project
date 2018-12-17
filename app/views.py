import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms import model_to_dict
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView, UpdateView

from app.form import Worcker, Company, Agahi
from app.models import company, worcker, agahi, shahr,ostan


class AgahiListView(ListView):
    model = agahi
    context_object_name = 'agahi'
"""class CompanyCreateView(CreateView):
    model = company
    form_class =Company
    success_url = reverse_lazy('login',kwargs={
    })


class CompanyUpdateView(UpdateView):
    model = company
    form_class = Company
    success_url = reverse_lazy('login')


class PersonCreateView(CreateView):
    model = worcker
    form_class = Worcker
    success_url = reverse_lazy('login')


class PersonUpdateView(UpdateView):
    model = worcker
    form_class = Worcker
    success_url = reverse_lazy('login')"""
#################################################


@csrf_protect
def login_(request):
    error=False
    if request.POST:
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        user= authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            error = True
            return render(request,'app/login.html',locals())
    return render(request, "app/login.html",locals())


def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")



def search(requet):
    if requet.GET and requet.GET.get("search"):
        agah = agahi.objects.filter(discriptation__icontains=requet.GET.get("search"))
        print(agah)
        return render(requet, "app/agahi_list.html", {"agahi": agahi})
    return HttpResponseRedirect('/')

################################################
def load_cities(request):
    country_id = request.GET.get('country')
    cities = shahr.objects.filter(ostan=country_id).order_by('name')
    return render(request, 'app/view.html', {'cities': cities})
##########################################################

#def home(request):
 #   a = agahi.objects.filter(active=True)
  #  return render(request, 'app/home.html', {
   #     'agahi': agahi,
    #}
     #             )


def signup_user(request):
    if request.POST:
        form = Worcker(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            global verify_user
            verify_user = str(random.randint(1, 99999))
            send_mail("verify", ("your verify code is " + verify_user), 'verifyUserSign@gmail.com', (cd['email'],))
            global form_user
            form_user = cd
            return HttpResponseRedirect('/verify_user/')
        return render(request, 'app/worcker_form.html', {'form': form})
    return render(request, 'app/worcker_form.html', {'form': Worcker})


def verify_user(request):
    if request.POST:
        global verify_user
        code = request.POST.get('code')
        if code == verify_user:
            global form_user
            print(form_user)
            a = worcker(active=form_user['active'],
                        first_name=form_user['first_name'],
                        last_name=form_user['last_name'],
                        username=form_user['username'],
                        password=form_user['password'],
                        email=form_user['email'],
                        id1=form_user['id1'],
                        sex1=form_user['sex1'],
                        marry_type1=form_user['marry_type1'],
                        birthday=form_user['birthday'],
                        mobile=form_user['mobile'],
                        phone=form_user['phone'],
                        madrak1=form_user['madrak1'],
                        education=form_user['education'],
                        ostan1=form_user['ostan1'],
                        shahr1=form_user['shahr1'],
                        exprience1=form_user['exprience1'],
                        job1=form_user['job1'],
                        job_field1=form_user['job_field1'],
                        job_type1=form_user['job_type1'],
                        address=form_user['address'],
                        pay=form_user['pay'],
                        pers_pictuare=form_user['pers_pictuare'],
                        rez_picture=form_user['rez_picture'])
            a.save()
            u=User.objects.create_user(username=form_user['username'],password=form_user['password'],
                                       first_name='worcker')
            u.save()
            return HttpResponseRedirect('/login/')
    return render(request, 'app/verify_user.html')


def signup_company(request):
    if request.POST:
        form = Company(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            global verify_company
            verify_company = str(random.randint(1, 99999))
            send_mail("verify", ("your verify code is " + verify_company), 'verifyUserSign@gmail.com', (cd['email'],))
            global form_company
            form_company = cd
            return HttpResponseRedirect('/verify_company/')
        return render(request, 'app/company_form.html', {'form': form})
    return render(request, 'app/company_form.html', {'form': Company})


def verify_company(request):
    if request.POST:
        global verify_company
        code = request.POST.get('code')
        if code == verify_company:
            global form_company
            print(form_company)
            b= company.objects.create(active=form_company['active'],
                                      username=form_company['username'],
                                      company_name=form_company['company_name'],
                                      modir_name=form_company['modir_name'],
                                      password=form_company['password'],
                                      email=form_company['email'],
                                      id1=form_company['id1'],
                                      id_date=form_company['id_date'],
                                      modirn=form_company['modirn'],
                                      member_n=form_company['member_n'],
                                      compane_type=form_company['compane_type'],
                                      work_type=form_company['work_type'],
                                      ostan=form_company['ostan'],
                                      shahr=form_company['shahr'],
                                      job_field=form_company['job_field'],
                                      job_type=form_company['job_type'],
                                      address=form_company['address'],
                                      web=form_company['web'],
                                      #logo_picture=form_company['logo_picture'],
                                      #rez_picture=form_company['rez_picture'])
                                      )
            print(b)
            #b.save()
            u=User.objects.create_user(username=form_company['username'],password=form_company['password'],
                                       first_name='company')
            u.save()
            return HttpResponseRedirect('/login/')
    return render(request, 'app/verify_company.html')

@login_required(login_url='login/')
def profile(request):
    if request.user.first_name =='worcker':
        u=worcker.objects.get(username=request.user.username)
        return render(request,'app/worcker_profile.html',{'form':u})
    elif request.user.first_name=='company':
        u=company.objects.get(username=request.user.username)
        return render(request,'app/company_profile.html',{'form':u})

@login_required(login_url='login/')
def edit_profile(request):
    if request.POST:
        if request.user.first_name == 'worcker':
            pass
        elif request.user.first_name == 'company':
            a=company.objects.get(username=request.POST.get('username'))
            a.active=bool(request.POST.get('active'))
            a.password=request.POST.get('password')
            a.company_name=(request.POST.get('company_name'))
            a.email=request.POST.get('email')
            a.ostan=ostan.objects.get(id=request.POST.get('ostan'))
            a.shahr=shahr.objects.get(id=request.POST.get(''))
            a.save()
            return HttpResponseRedirect('/profile/')
    else:
        if request.user.first_name == 'worcker':
            u = worcker.objects.get(username=request.user.username).values()
            u = model_to_dict(u)
            form = Worcker(initial=u)
            return render(request, 'app/editworcker_profile.html', {'form': form})
        elif request.user.first_name == 'company':
            u = company.objects.get(username=request.user.username)
            u = model_to_dict(u)
            print(u)
            form = Company(initial=u)
            return render(request, 'app/editcompany_profile.html', {'form': form})


@login_required(login_url='login/')
def addagahi(request):
    if request.POST:
        form=Agahi(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            compay1=company.objects.get(username=request.user.username)
            a=agahi.objects.create(company1=compay1,
                                   discriptation=cd['discriptation'])
            return render(request,'app/success.html')
        return render(request,'app/agahi.html',{'form':form})
    return render(request,'app/agahi.html',{'form':Agahi})