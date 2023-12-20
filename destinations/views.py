from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView 
from .models import Destination
from .forms import DestinationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages

class Destinations(ListView):
    """
    View all destination reviews
    """
    template_name = 'destinations/destinations.html'
    model = Destination
    context_object_name = 'destinations'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            destinations = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(brief__icontains=query) |
                Q(review__icontains=query)
            )
        else:
            destinations = self.model.objects.all()
        return destinations


class DestinationFullReview(DetailView):
    """
    View a single full destination review
    """
    template_name = 'destinations/destination_full_review.html'
    model = Destination
    context_object_name = 'destination'


class AddDestination(LoginRequiredMixin, CreateView):
    """
    Add a destination review view
    """
    template_name = 'destinations/add_destination.html'
    model = Destination
    success_url = '/destinations/destinations/'
    form_class = DestinationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddDestination, self).form_valid(form)


class EditDestination(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a destination review
    """
    template_name = 'destinations/edit_destination.html'
    model = Destination
    form_class = DestinationForm
    success_url = '/destinations/destinations/'

    def form_valid(self, form):
        """ 
        Show toast on successful editing of destination review 
        """
        messages.success(
            self.request,
            'Changes Successfully Updated!'
        )
        return super(EditDestination, self).form_valid(form)


    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteDestination(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a destination review
    """
    model = Destination
    success_url = '/destinations/destinations/'

    def form_valid(self, form):
        """ 
        Show toast message on successful deletion of a destination review
        """
        messages.success(
            self.request,
            'Successfully Deleted Destination Review'
        )
        return super(DeleteDestination, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user