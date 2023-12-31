from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages


class Profiles(TemplateView):
    """
    User profile view
    """
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile)
        }

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a profile
    """
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.success_url = f"/profiles/user/{self.request.user.username}"

        messages.success(
            self.request,
            'Profile Successfully Updated!'
        )
        return super(EditProfile, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
