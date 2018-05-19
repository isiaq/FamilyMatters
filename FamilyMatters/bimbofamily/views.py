from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Quote, Author, Category,Language


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_quotes=Quote.objects.all().count()
    # Available quotes (status = 'a')
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render_to_response('bimbofamily/index.html',{'num_quotes': num_quotes})
# Create your views here.
