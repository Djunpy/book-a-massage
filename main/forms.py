import datetime
from django import forms
from django.core.mail import send_mail

from django_website.settings import EMAIL_HOST_USER
from .models import Comment, Booking


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



class BookingForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email'}))
    the_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    the_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Booking
        fields = ('username', 'email', 'the_date', 'the_time')

    def send_email_feedback(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        date = self.cleaned_data['the_date']
        time = self.cleaned_data['the_time']



