from django.shortcuts import render, HttpResponse

# Create your views here.
def say_helllo(request):
    return HttpResponse("Hello!")