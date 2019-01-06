from django import views
from django.views import generic


class HomeView(generic.TemplateView):
    """ shows the homepage """
    template_name = 'home.html'
