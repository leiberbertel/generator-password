from django.shortcuts import render
# from django.http import HttpResponse
import random


def home(request):
    return render(request, "generator/home.html")

def about(request):
    return render(request, "generator/about.html")

def password(request):

    characters = list("abcdefghijklmnñopqrstuvwxyz")
    gerenated_password = ""
    
    length = int(request.GET.get("length"))    

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWYZ"))

    if request.GET.get("special"):
        characters.extend(list("#@~%_-+*?&()"))

    if request.GET.get("number"):
        characters.extend(list("0123456789"))


    for x in range (length):
        gerenated_password += random.choice(characters)
    
    return render(request, "generator/password.html", {"password": gerenated_password})