from django.shortcuts import render
from django.shortcuts import HttpResponse
def about(request):
    # return HttpResponse (' hi there Im here ')
    return render (request , 'about.html')

def home(request):
    # return HttpResponse('and this is home ')
    return render (request , 'home.html')