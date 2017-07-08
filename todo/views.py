from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Item

import os
import json
import random
from django.forms.models import model_to_dict

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from datetime import datetime

@login_required(login_url='/login/')
def index(request):
    '''index will populate the page with items from the database'''
    template_name = 'todo/index.html'
    context_object_name = 'item_list'
    # Split the items based on whether or not the due date has passed
    todo_items = Item.objects\
        .filter(due_date__gte=timezone.now())\
        .order_by('due_date')
    past_items = Item.objects\
        .filter(due_date__lt=timezone.now())\
        .order_by('due_date')

    return render(request, template_name,
                  {context_object_name: todo_items,
                   'past_items': past_items})

@login_required(login_url='/login/')
def complete_item(request):
    '''Update an item's complete status via an ajax request'''
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
    # Update the item's compete status and save it to the database
    item.complete = bool_complete
    item.save()

    # Return the JsonResponse - the returned dict is not used for anything
    return JsonResponse({'tmp': 'success'}, safe=False)

@login_required(login_url='/login/')
def show_item(request):
    '''Return a specific item using passed in primary key via ajax request'''
    try:
        item_id = request.GET['id']
        item_select = get_object_or_404(Item, pk=item_id)
    except:
        print("Error at todo.view.ajax")

    # To format the data correctly, model_to_dict is used
    pre_data = model_to_dict(item_select)
    # Convert the date fields from datetime objects to strings
    pre_data['add_date'] = str(pre_data['add_date'])
    pre_data['due_date'] = str(pre_data['due_date'])
    pre_data['start_date'] = str(pre_data['start_date'])

    # Dump data and return it
    data = json.dumps(pre_data)
    return JsonResponse(data, safe=False)

@login_required(login_url='/login/')
def add_item_public(request):
    desc_options = ["Complete work on next side project",
                    "Get milk",
                    "Finish documentation",
                    "Learn New Language/Framework (Java, NodeJS, Scala, etc.)",
                    "Finish the book"]
    imp_options = ["Sharpen my skills and bolster the portfolio.",
                   "I don't want to eat cereal with water. Get milk.",
                   "Code can be better understood by others (and future me)",
                   "Expand my capabiliities so I can build new things",
                   "Gain a new perspective and grow as a person"]
    '''Only the date fields may be modified'''
    def convert_date(date_string):
        '''Helper function to convert dates as strings to datetime objects'''
        return datetime.strptime(date_string, '%m/%d/%Y')

    if 'add_button' in request.POST:
        if len(request.POST['start']) <= 10 or len(request.POST['due']) <= 10:
            try:
                option = random.randint(0, 4)
                # Attempt to fill out a new item and save it to the database
                title_text = 'Preset Example Title ' + str(option)
                desc_text = desc_options[option]
                impact_text = imp_options[option]
                start_date = convert_date(request.POST['start'])
                due_date = convert_date(request.POST['due'])
                complete = False
                priority = -1
                add_date = timezone.now()

                new_item = Item(title_text=title_text,
                                desc_text=desc_text,
                                impact_text=impact_text,
                                start_date=start_date,
                                due_date=due_date,
                                priority=priority,
                                complete=complete,
                                add_date=add_date)
                new_item.save()

            except:
                # If it didn't work, assume the provided data was invalid and
                # request user try again.
                messages.warning(request, "Input Not Valid - Please Try Again")
                HttpResponseRedirect(request.path)
        else:
            # If it didn't work, assume the provided data was invalid and
            # request user try again.
            messages.warning(request, "Date Not Valid")
            HttpResponseRedirect(request.path)

    # Used instead of redirect so that back button goes back to todo page
    return HttpResponseRedirect(reverse('todo:index'))

@login_required(login_url='/login/')
def add_item(request):
    '''Add a new item from a form via POST method'''
    def convert_date(date_string):
        '''Helper function to convert dates as strings to datetime objects'''
        return datetime.strptime(date_string, '%m/%d/%Y')

    if 'add_button' in request.POST:
        # Is password correct?
       
        try:
            # Attempt to fill out a new item and save it to the database
            title_text = request.POST['title']
            desc_text = request.POST['desc']
            impact_text = request.POST['impact']
            start_date = convert_date(request.POST['start'])
            due_date = convert_date(request.POST['due'])
            complete = False
            priority = -1
            add_date = timezone.now()

            new_item = Item(title_text=title_text,
                            desc_text=desc_text,
                            impact_text=impact_text,
                            start_date=start_date,
                            due_date=due_date,
                            priority=priority,
                            complete=complete,
                            add_date=add_date)
            new_item.save()

        except:
            # If it didn't work, assume the provided data was invalid and
            # request user try again.
            messages.warning(request, "Input Not Valid - Please Try Again")
            HttpResponseRedirect(request.path)
    # Used instead of redirect so that back button goes back to todo page
    return HttpResponseRedirect(reverse('todo:index'))
