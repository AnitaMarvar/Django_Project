from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("basics",views.basics,name="basics"),
    path("emergency_numbers",views.emergency_numbers,name="emergency_numbers"),
    path("cpr",views.cpr,name="cpr"),
    path("burns",views.burns,name="burns"),
    path("tips_tutorials",views.tips_tutorials,name="tips_tutorials"),
    path("about",views.about,name="about"),
    path("cuts",views.cuts,name="cuts"),
    path("choking",views.choking,name="choking"),
    path("contacts",views.contacts,name="contacts"),
    





]