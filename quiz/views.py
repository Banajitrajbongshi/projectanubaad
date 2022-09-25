from django.shortcuts import render
from django.http import HttpResponse
from .models import questions_base
# Create your views here.
def quiz_homepage(request):
    data=questions_base.objects.all()
    info={
        'new':data,
    }
    return render(request,'quiz_page.html',info)

def result_page(request):
    pass