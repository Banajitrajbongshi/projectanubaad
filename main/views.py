from django.shortcuts import render
from django.http import HttpResponse
from main.models import recieve_content

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def donation(request):
    return render(request,'donation.html')

def form(request,*args, **kwargs):
    if request.method=="POST":
        name=request.POST["name"]
        mail=request.POST["email"]
        address=request.POST["address"]
        content=request.POST["content"]
        data=recieve_content(name=name,email=mail,address=address,content=content)
        data.save()
        new_line={
            "username":name
        }
        return render(request,'thanks.html',new_line)
    return render(request,'form.html')