
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponseRedirect
from blog.forms import SignUp,SignIn,PostForm
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    posts =Post.objects.all()

    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,"blog/contact.html")

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,"blog/dashboard.html",{'posts':posts,"full_name":full_name,"groups":gps})
    else:
        return HttpResponseRedirect("/accounts/login/")

     

def register(request):
    if request.method == "POST":
        fm = SignUp(request.POST)
        if fm.is_valid():
            user = fm.save()
            group= Group.objects.get(name="Author")
            user.groups.add(group)
            messages.success(request,'Congratulations You have become an Author')
    else:
        fm = SignUp()
    return render(request,"blog/register.html",{"form":fm})

def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignIn(request = request,data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname,password = upass)
                if user:
                    login(request,user)
                    messages.success(request,"Login successful!")
                    return HttpResponseRedirect("/dashboard/")
            else:
                fm = SignIn()



        else:
            fm=SignIn()
        
        return render(request,"blog/login.html",{"form":fm})
    else:
        return HttpResponseRedirect('/dashboard/')
def signout(request):
    logout(request)
    return HttpResponseRedirect("/")

def add_new_post(request):
    
    if request.user.is_authenticated:
        if request.method =="POST":
           
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Your post added successfully")
                form = PostForm()
        else:
            form = PostForm()


        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect("/accounts/login/")

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, "Your post updated successfully")
        else:
            pi = Post.objects.get(pk = id)
            form = PostForm(instance=pi)

        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect("/accounts/login/")


def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method =="POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect("/accounts/login/")








