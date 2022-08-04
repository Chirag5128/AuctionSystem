from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse(render(request, 'homepage.html',{}))