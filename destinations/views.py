from django.views.generic import CreateView
from .models import Destination
from .forms import DestinationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
