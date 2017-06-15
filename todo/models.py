from django.db import models


class Item(models.Model):
    '''Represents an item on a todo list, such as user, desc, etc.
    '''
    title_text = models.CharField(max_length=200, default="")
    desc_text = models.TextField()
    impact_text = models.TextField()
    add_date = models.DateTimeField('date added')
    due_date = models.DateTimeField('complete by')
    priority = models.FloatField()
    complete = models.BooleanField(default=False)

    def __repr__(self):
        pass

    def __str__(self):
        return self.title_text
