from django.db.models import Q
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import*
from django.db.models import Q
from datetime import date
from .forms import*
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'fake.html')

def index(request,dil):
    qp=0
    wr=uniwersitetler.objects.filter(link__startswith='www')
    for i in wr:
        qp+=1
        print(i)
    print(qp)
    video=bash_video.objects.all()[:2]
    tkm_uniwersitet=uniwersitetler.objects.filter(yurt=1)[:12]
    global_uniwersitetler=uniwersitetler.objects.filter(~Q(yurt=1))[:12]
    context={
        'videos':video,
        'tkm_uniwersitet':tkm_uniwersitet,
        'global_uniwersitet':global_uniwersitetler,
        'tazelikler':news.objects.all()[:12],
        'ln':dil,
        'yurtlar':yurtlar.objects.all(),
        'san':'san'
    }
    return render(request,'index.html',context)

def teswir(request,id,dil):
    teswirler=Teswir.objects.filter(uniwersitet=id)[:100]
    a1=uniwersitetler.objects.get(id=id)
    context={
        'a1':a1,
        'form':gosulmak_form(),
        'teswirler':teswirler,
        'ln':dil,
        'habar':a1,
        'page':'teswir',
        'yurtlar':yurtlar.objects.all()
    }
    if request.method == "POST":
        form = gosulmak_form(request.POST)
        if form.is_valid():
            pp=register.objects.filter(parol=request.POST['password'],phone=request.POST['phone'])
            if len(pp)==0:
                register(at=request.POST['at'],
                        gmail=request.POST['email'],
                        parol=request.POST['password'],
                        phone=request.POST['phone']).save()
                context['v1']='Üstünlikli sanawymyza goşuldyňyz!'
                context['v3']='success'                
            else:
                context['v2']='Siziň girizen maglumatyňyz ozal ulanyşda, maglumatyňyzyň dogrulygyny barlaň!'
                context['v3']='error'
        else:
            context['v2']='Nädogry maglumat girizdiňiz maglumatyňyzyň dogrulygyn barlaň!'
            context['v3']='error'
    return render(request,'teswir.html',context)

def beyan(request,id,dil):
    teswirler=Teswir.objects.filter(uniwersitet=id)
    a1=uniwersitetler.objects.get(id=id)
    context={'a1':a1,'form':gosulmak_form(),'yurtlar':yurtlar.objects.all(),'teswirler':teswirler,'ln':dil,'page':'page'}
    date1=date.today()
    if request.method=='POST':
        a8=register.objects.filter(parol=request.POST['parol'])
        if len(a8)!=0:
            a9=register.objects.get(parol=request.POST['parol'])
            beyanFORM = request.POST['beyan']
            u=uniwersitetler.objects.get(id=id)
            taze=Teswir(at=a9.at,uniwersitet=u,beyan=beyanFORM,wagt=date1)
            taze.save()
            context['v1']='Üstünlikli teswir iberildi!'
            context['v3']='success'
        else:
            context['v2']='Biziň sanawymyza goşulyň ýada açar sözüni dogry ýazanlygyňyzy anyklaň!'
            context['v3']='info'
            
    return render(request,'teswir.html',context)

def dil_(request,dil,page):
    if page=='yurt_uni':
        return redirect('index',dil)
    return redirect(page,dil)

def dil_1(request,dil,page,id):
    return redirect(page,id,dil)
    

def each_news(request,id,dil):
    habar=news.objects.get(id=id)
    habarlar=news.objects.filter(~Q(id=id))[:5]
    context={
        'habar':habar,
        'habarlar':habarlar,
        'ln':dil,
        'page':'each_news',
        'yurtlar':yurtlar.objects.all()
    }
    return render(request,'news.html',context)

def all_news(request,dil):
    context={
        'all_news':news.objects.all()[:100],
        'ln':dil,
        'page':'all_news',
        'yurtlar':yurtlar.objects.all()

    }
    return render(request,'all_news.html',context)

def yurt_uni(request,dil):
    context={'ln':dil}
    if request.method=='POST':
        if dil=='tm':
            a=yurtlar.objects.get(at_tm=request.POST['yurt'])
        elif dil=='ru':
            a=yurtlar.objects.get(at_ru=request.POST['yurt'])
        elif dil=='en':
            a=yurtlar.objects.get(at_en=request.POST['yurt'])
        b=uniwersitetler.objects.filter(yurt=a.id)
        san=uniwersitetler.objects.filter(yurt=a.id).count()
        context['okuwlar']=b
        context['yurt']=a
        context['yurtlar']=yurtlar.objects.all()
        context['san']=san
        context['page']=request
        return render(request,'sorted_uniw.html',context)
    else:
        return redirect('index',context)
    