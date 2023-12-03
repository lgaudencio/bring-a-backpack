from django.views.generic import CreateView
from .models import Photography
from .forms import PhotographyForm


class AddPhotography(CreateView):
    """
    Add photography view
    """
    template_name = 'photography/add_photography.html'
    model = Photography
    form_class = PhotographyForm
    success_url = '/photography/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPhotography, self).form_valid(form)
