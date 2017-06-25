from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views import generic

from django.http import JsonResponse

from django.views.generic.edit import FormView

from django.utils import timezone

from django.contrib import messages

from .models import Item

import json
import datetime
from django.forms.models import model_to_dict


def index(request):
    template_name = 'todo/index.html'
    context_object_name = 'item_list'
    todo_items = Item.objects.order_by('-due_date')
    item_select = todo_items[0]
    return render(request, template_name,
                  {context_object_name: todo_items,
                   'item_select': item_select})


def ajax(request):
    try:
        id = request.GET['id']
        item_select = get_object_or_404(Item, pk=id)
    except:
        print("Error at todo.view.ajax")

    pre_data = model_to_dict(item_select)
    pre_data['add_date'] = str(pre_data['add_date'])
    pre_data['due_date'] = str(pre_data['due_date'])
    pre_data['start_date'] = str(pre_data['start_date'])
    data = json.dumps(pre_data)
    return JsonResponse(data, safe=False)
