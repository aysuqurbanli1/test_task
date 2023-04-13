from django.shortcuts import render,redirect
from account.forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from account.models import Instagram
from account.tasks import instagram_data
from django.http import HttpResponse




def login_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,"login.html",{
                "error":"Incorrect username or password"
            })

        
    return render(request,'login.html')





def register_request(request):
    if request.user.is_authenticated:
        return redirect('index')
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                user = form.save()
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('login')
        context = {
            'form': form
        }   
        return render(request,'register.html', context)
    else:
        return redirect('')
    







def index(request):
    instagram_data=Instagram.objects.all().first()
    context={
        'instagram_data':instagram_data,
    }
    return render(request,'index.html',context)


def logout_request(request):
    logout(request)
    return redirect('index')


def instagram(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if Instagram.objects.filter(username=username).exists():
            return redirect('/')
        else:
            instagram=Instagram.objects.create(username=username,password=password)
            instagram.save()
            instagram_data()
            return redirect('/')
    
    return render(request,'instagram.html')






    
