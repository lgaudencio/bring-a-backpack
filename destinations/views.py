from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView 
from .models import Destination
from .forms import DestinationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class Destinations(ListView):
    """
    View all destination reviews
    """
    template_name = 'destinations/destinations.html'
    model = Destination
    context_object_name = 'destinations'


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
    success_url = '/destinations/'
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
    success_url = '/destinations/'

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteDestination(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a destination review
    """
    model = Destination
    success_url = '/destinations/'

    def test_func(self):
        return self.request.user == self.get_object().user