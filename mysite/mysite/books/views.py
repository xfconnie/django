from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book, Publisher

# Create your views here.

def search_form(request):
    errors=[]
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Publisher.objects.filter(name__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    
    return render_to_response('search_form.html',{'errors':errors})

