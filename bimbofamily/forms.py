from django import forms
from bimbofamily.models import Album

class ContactForm(forms.Form):
	name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please Enter your name'}))
                        
	from_email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Please Enter your email'}))

	subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Please Enter subject of your maill'}))
                           
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Please Enter your Message'}))


                               
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    zip = forms.FileField(required=False)


       