from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Item

import os
import json
from django.forms.models import model_to_dict

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.utils import timezone
from django.contrib import messages
from datetime import datetime


def index(request):
    template_name = 'todo/index.html'
    context_object_name = 'item_list'
    todo_items = Item.objects.filter(due_date__gt=timezone.now()).order_by('due_date')
    return render(request, template_name,
                  {context_object_name: todo_items,
                   'refresh': True})


def complete_item(request):
    try:
        item_id = request.GET['id']
        complete = request.GET['complete']
        item = get_object_or_404(Item, pk=item_id)
    except:
        print("Error at todo.view.ajax")
    if complete == "false":
        bool_complete = False
    elif complete == "true":
        bool_complete = True
    else:
        print("ERROR WITH complete_item")
    item.complete = bool_complete
    item.save()

    return JsonResponse({'tmp': 'success'}, safe=False)


def ajax(request):
    try:
        item_id = request.GET['id']
        item_select = get_object_or_404(Item, pk=item_id)
    except:
        print("Error at todo.view.ajax")

    pre_data = model_to_dict(item_select)
    pre_data['add_date'] = str(pre_data['add_date'])
    pre_data['due_date'] = str(pre_data['due_date'])
    pre_data['start_date'] = str(pre_data['start_date'])
    data = json.dumps(pre_data)
    return JsonResponse(data, safe=False)


def simple_auth(password):
    if password == os.environ.get('TODO_DJ_ADD_PASS'):
        return True
    else:
        return False


def add_item(request):
    def convert_date(date_string):
        return datetime.strptime(date_string, '%m/%d/%Y')
    print("test")
    if 'add_button' in request.POST:
        if simple_auth(request.POST['password']):
            try:
                title_text = request.POST['title']
                desc_text = request.POST['desc']
                impact_text = request.POST['impact']
                start_date = convert_date(request.POST['start'])
                due_date = convert_date(request.POST['due'])
                complete = False
                priority = -1
                add_date = timezone.now()

                new_rec = Item(title_text=title_text,
                               desc_text=desc_text,
                               impact_text=impact_text,
                               start_date=start_date,
                               due_date=due_date,
                               priority=priority,
                               complete=complete,
                               add_date=add_date)
                new_rec.save()

            except:
                messages.warning(request, "Input Not Valid - Please Try Again")
                HttpResponseRedirect(request.path)
        else:
            messages.warning(request, "Password Not Valid")
            HttpResponseRedirect(request.path)

    # Used instead of redirect so that back button goes back to calc page
    return HttpResponseRedirect(reverse('todo:index'))
