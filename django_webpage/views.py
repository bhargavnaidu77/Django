from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def Bhargav(request):
    return HttpResponse('''<h1>Hey Bhargav</h1>''')

