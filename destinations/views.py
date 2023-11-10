from django.views.generic import CreateView
from .models import Recipe


class AddDestination(CreateView):
    """
    Add a destination review view
    """
    template_name = 'destinations/add_destination.html'
    model = Destination
    success_url = '/destinations/'
