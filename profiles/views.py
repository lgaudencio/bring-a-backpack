from django.views.generic import TemplateView, UpdateView
from .models import Profile
from .forms import Profile


class Profiles(TemplateView):
    """
    User profile view
    """
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            'profile': profile
        }

        return context


class EditProfile(UpdateView):
    """
    Edit a profile
    """
    form_class = ProfileForm
    model = Profile 

    def form_valid(self, form):
        self.success_url = f"/profile/view/{self.kwargs['pk']}"
        return super().form_valid(form)