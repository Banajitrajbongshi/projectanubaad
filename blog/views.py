from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost
# Create your views here.
def homepage(request):
    blog_post_home=blogpost.objects.all()
    data={
        "products":blog_post_home
    }
    return render(request,'homepage.html',data)

def post(request,my_id):
    info=blogpost.objects.filter(post_id=my_id)
    return render(request,'post.html',{'data':info[0]})