from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Photography
from .forms import PhotographyForm
from django.contrib import messages


class PhotographyList(ListView):
    """
    View all photography posts
    """
    template_name = 'photography/photography.html'
    model = Photography
    context_object_name = 'photography_list'


class PhotographyDetail(DetailView):
    """
    View a single photography post
    """
    template_name = 'photography/photography_full_post.html'
    model = Photography
    context_object_name = 'photography'


class AddPhotography(LoginRequiredMixin, CreateView):
    """
    Add photography view
    """
    template_name = 'photography/add_photography.html'
    model = Photography
    form_class = PhotographyForm
    success_url = '/photography/photography_list/'

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.success(
            self.request,
            'Photography Post Successfully Created'
        )
        return super(AddPhotography, self).form_valid(form)


class EditPhotography(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a photography post
    """
    template_name = 'photography/edit_photography.html'
    model = Photography
    form_class = PhotographyForm
    success_url = '/photography/photography_list/'

    def form_valid(self, form):
        """
        Show toast on successful editing of photography post
        """
        messages.success(
            self.request,
            'Changes Successfully Updated!'
        )
        return super(EditPhotography, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeletePhotography(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a photography post
    """
    model = Photography
    success_url = '/photography/photography_list/'

    def form_valid(self, form):
        """
        Show toast message on successful deletion of a photography post
        """
        messages.success(
            self.request,
            'Successfully Deleted Photography Post'
        )
        return super(DeletePhotography, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
