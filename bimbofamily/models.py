from django.db import models
from django.urls import reverse #Used to generate urls by reversing the URL patterns
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title

class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

class Category(models.Model):
    """
    Model representing a quote category (e.g. Science, Life, Humor).
    """
    name = models.CharField(max_length=200, help_text="Enter a Quote category (e.g. Science, Life and Humor etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
        
class Language(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200, help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
        
class Quote(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
      # Foreign Key used because book can only have one author, but authors can have multiple books
      # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
#    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    category = models.ManyToManyField(Category, help_text="Select a category for this quote")
      # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
      # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
      
    def display_category(self):
        """
        Creates a string for the Category. This is required to display category in Admin.
        """
        return ', '.join([ category.name for category in self.genre.all()[:3] ])
        display_category.short_description = 'Category'
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular quote instance.
        """
        return reverse('quote-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        
        
import uuid # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower

#class BookInstance(models.Model):
#    """
#    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
#    """
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
#    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
#    imprint = models.CharField(max_length=200)
#    due_back = models.DateField(null=True, blank=True)
#    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#    
#    @property
#    def is_overdue(self):
#        if self.due_back and date.today() > self.due_back:
#            return True
#        return False
#        
#
#    LOAN_STATUS = (
#        ('d', 'Maintenance'),
#        ('o', 'On loan'),
#        ('a', 'Available'),
#        ('r', 'Reserved'),
#    )
#
#    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')
#
#    class Meta:
#        ordering = ["due_back"]
#        permissions = (("can_mark_returned", "Set book as returned"),)   
#
#    def __str__(self):
#        """
#        String for representing the Model object.
#        """
#        #return '%s (%s)' % (self.id,self.book.title)
#        return '{0} ({1})'.format(self.id,self.book.title)
#        

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)