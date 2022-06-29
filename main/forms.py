from django import forms

from .models import Comment, Booking


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('username', 'email', 'the_date')

