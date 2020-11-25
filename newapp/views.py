from django.shortcuts import render

from django.shortcuts import  HttpResponse, redirect 
from django.http import JsonResponse
#1 
def root_method(request):
     return redirect("blogs/")
    #  return HttpResponse("redirect !")


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
# def index2(request, id):
#     return HttpResponse("the second path!")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog" )

def create(request):
     return redirect("/firstapp/")
    #  return HttpResponse("redirect !")
def show(request, num):
    return HttpResponse(f"placeholder to display blog number {num}")
def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request , num):
     return redirect("/firstapp/")

def jsonreturn(request):
    return JsonResponse(request.data)

    
