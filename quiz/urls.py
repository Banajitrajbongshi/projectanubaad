from django.urls import path
from . import views

urlpatterns = [
    path("",views.quiz_homepage,name="quiz_homepage"),
    path("",views.result_page,name="result")
]