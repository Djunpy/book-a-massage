
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Massage, Booking, Comment
from .forms import CommentForm, BookingForm
from .mixins import CommentActionMixin
from .task import send_feedback_email_task, send_comment_task


class HomePageView(generic.ListView):
    model = Massage
    template_name = 'home.html'

    def get_queryset(self):
        return Massage.objects.all()[:4]


class MassagesView(HomePageView):
    template_name = 'massage_list.html'


class MassagesDetail(generic.DetailView):
    model = Massage
    template_name = 'massage_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_comment'] = CommentForm()
        context['booking_form'] = BookingForm()
        return context


class BookingView(generic.View):

    def post(self, request, pk):
        massage = get_object_or_404(Massage, pk=pk)
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            instance = booking_form.save(commit=False)
            instance.massage = massage
            instance.save()
            send_feedback_email_task.delay(instance.pk)
            return redirect(massage.get_absolute_url())
        else:
            booking_form = BookingForm(request.POST)


class AddComment(generic.View):

    def post(self, request, pk):
        message = get_object_or_404(Massage, pk=pk)
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            instance = form_comment.save(commit=False)
            instance.massage = message
            instance.save()
            send_comment_task.delay(instance.pk)
            return redirect(message.get_absolute_url())
        else:
            form_comment = CommentForm(request.POST)

