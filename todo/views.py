from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic

from django.views.generic.edit import FormView

from django.utils import timezone

from django.contrib import messages

from .models import Item


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.order_by('-priority')


def AddItem(request):
    if 'submit' in request.POST:
        try:
            title_text = request.POST['op_a']
            desc_text = request.POST['op']
            impact_text = request.POST['op_b']
            add_date = request.POST['op_b']
            due_date = request.POST['op_b']
            priority = request.POST['op_b']
            new_item = Item(title_text, desc_text, impact_text, add_date,
                            due_date, priority)
            new_item.save()
        except:
            messages.warning(request, "Input Not Valid - Please Try Again")
            HttpResponseRedirect(request.path)
    # Used instead of redirect so that back button goes back to calc page
    return HttpResponseRedirect(reverse('calc:generic_index'))
