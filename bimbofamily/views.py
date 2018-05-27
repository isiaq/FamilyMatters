from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Quote, Author, Category,Language
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import smtplib
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from fm.views import AjaxCreateView
from bimbofamily.forms import ContactForm
from django.template import RequestContext


class FeedbackCreateView(AjaxCreateView):
    form_class = ContactForm

from bimbofamily.models import Album, AlbumImage
def media(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginator(list, 10)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

    return render(request, 'gallery.html', { 'albums': list })

class AlbumDetail(DetailView):
     model = Album

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

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
            return redirect('successView')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def about(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
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
            # return redirect('success')
    return render(request, "bimbofamily/about.html", {'form': form})


def session(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # subject = form.cleaned_data['subject']
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
            return redirect('/success')
    return render(request, "session.html", {'form': form})
def connect(request):
    return render_to_response('bimbofamily/connect.html')

#def media(request):
#    return render_to_response('bimbofamily/media.html')
def memorial(request):
    return render_to_response('bimbofamily/memorial.html')

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