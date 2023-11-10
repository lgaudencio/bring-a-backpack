from django.views.generic import CreateView
from .models import Recipe
from .forms import DestinationForm


class AddDestination(CreateView):
    """
    Add a destination review view
    """
    template_name = 'destinations/add_destination.html'
    model = Destination
    success_url = '/destinations/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddDestination, self).form_valid(form)
