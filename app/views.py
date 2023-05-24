from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('this is first functoin welcome to first')
def second(request):
    return HttpResponse('this is second functoin welcome to second')
def three(request):
    return render(request, 'home.html')
def four(request):
    return render(request, 'home1.html')

