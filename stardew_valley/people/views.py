from django.shortcuts import render
from django.views import generic

from . import models


class IndexView(generic.TemplateView):
    """ shows the index for the Villagers app """
    template_name = 'people/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['villagers'] = models.Villager.objects.all()
        return context


class VillagerDetailView(generic.DetailView):
    """ Shows details about a specific villager """
    model = models.Villager
    context_object_name = 'villager'
