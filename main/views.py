from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Massage, Booking, Comment
from .forms import CommentForm, BookingForm
from .mixins import CommentActionMixin


class HomePageView(generic.ListView):
    model = Massage
    template_name = 'home.html'


class MassagesView(HomePageView):
    template_name = 'massage_list.html'


class MassagesDetail(generic.DetailView):
    model = Massage
    template_name = 'massage_detail.html'


class AddComment(generic.View):

    success_msg = 'Отправлено'

    def post(self, request, pk):
        massage = get_object_or_404(Massage, id=pk)
        form = CommentForm(request.POST)
        success_msg = "Flavor created!"
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            body = request.POST.get('body')
            Comment.objects.update_or_create(
                name=name,
                email=email,
                body=body,
                massage=massage
            )
            messages.info(self.request, self.success_msg)
            return redirect(massage.get_absolute_url())
        else:
            form = CommentForm()


class AddBookingView(generic.View):

    success_msg = 'Отправлено'

    def post(self, request, pk):
        massage = get_object_or_404(Massage, id=pk)
        form = BookingForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            the_date = request.POST.get('the_date')
            Booking.objects.update_or_create(
                massage=massage,
                username=username,
                email=email,
                the_date=the_date
            )
            return redirect(massage.get_absolute_url())
        else:
            form = BookingForm()


