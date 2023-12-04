from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photography
from .forms import PhotographyForm


class PhotographyList(ListView):
    """ 
    View all photography posts
    """
    template_name = 'photography/photography.html'
    model = Photography 
    context_object_name = 'photography_list'


class AddPhotography(LoginRequiredMixin, CreateView):
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
