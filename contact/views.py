from django.views.generic import TemplateView


class Contact(TemplateView):
    """
    Create Contact page
    """
    template_name = 'contact/contact.html'
