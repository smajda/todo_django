from django.db import models


class Item(models.Model):
    '''Represents an item on a todo list, such as user, desc, etc.
    '''
    title_text = models.CharField(max_length=200, default="")
    desc_text = models.TextField()
    impact_text = models.TextField()
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    priority = models.FloatField()
    complete = models.BooleanField(default=False)
    add_date = models.DateTimeField()

    def __repr__(self):
        pass

    def __str__(self):
        return self.title_text
