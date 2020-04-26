from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import Tutorial,TutorialCategory,TutorialSeries
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            print(part_one)
            series_urls[m] = part_one.tutorial_slug
        
        return render(request=request,
                      template_name='main/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})

    tutorials=[t.tutorial_slug for t in Tutorial.objects.all()]

    if single_slug in tutorials:
        this_tutorial=Tutorial.objects.get(tutorial_slug=single_slug)
        tutorial_from_series=Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")
        this_tutorial_idx=list(tutorial_from_series).index(this_tutorial)
        print(this_tutorial_idx)
        return render(request,"main/tutorial.html",context={"tutorial":this_tutorial,"sidebar":tutorial_from_series,"this_tutorial_idx":this_tutorial_idx})

    return HttpResponse(f"{single_slug} does not corresponding anything")




def  homepage(request):
    return render(request,template_name='main/categories.html',context={'categories':TutorialCategory.objects.all()})

# def  homepage(request):
#     return render(request,template_name='main/home.html',context={'tutorials':Tutorial.objects.all()})


def register(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"New Account Has Been Created {username}")
            login(request,user)
            messages.info(request,f"You are logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")


    form=NewUserForm
    return render(request,"main/register.html",context={'form':form})



def logout_request(request):
    logout(request)
    messages.info(request,"Successfully Logged Out")
    return redirect('main:homepage')


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid Username or Password")
        else:
            messages.error(request,"Invalid name or password ")
    form=AuthenticationForm()
    return render(request,"main/login.html",{'form':form})
