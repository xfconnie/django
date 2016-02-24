from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse('home') 