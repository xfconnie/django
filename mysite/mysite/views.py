from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse('home')

def display_meta(request):
    values = request.META.items()
    values.sort()
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' %'\n'.join(html))
