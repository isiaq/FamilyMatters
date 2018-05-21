from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Quote, Author, Category,Language
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import smtplib

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            port=587
            host="smtp.gmail.com"
            email_conn = smtplib.SMTP(host, port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login("isiaq.ao@gmail.com", "Gbongy4sure!")
            try:
                email_conn.sendmail(from_email, 'diji.odutola@gmail.com',message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_quotes=Quote.objects.all()
    
    # Available quotes (status = 'a')
    num_authors=Author.objects.count()
    # The 'all()' is implied by default.


    
    # Render the HTML template index.html with the data in the context variable
    return render_to_response('bimbofamily/index.html',{'num_quotes': num_quotes})
# Create your views here.
from django.views import generic

class QuoteListView(generic.ListView):
    model = Quote
    context_object_name = 'my_quote_list'   # your own name for the list as a template variable
    queryset = Quote.objects.filter(title__icontains='be')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location