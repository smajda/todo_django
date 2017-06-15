from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.contrib import messages

from .models import Item


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.order_by('-priority')
# Create your views here.
