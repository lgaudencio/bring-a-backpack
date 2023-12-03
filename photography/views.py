from django.views.generic import CreateView
from .models import Photography


class AddPhotography(CreateView):
    """
    Add photography view
    """
    template_name = 'photography/add_photography.html'
    model = Photography
    success_url = '/photography/'
    