from django.db import models


class item(models.Model):
    '''Represents an item on a todo list, such as user, desc, etc.
    '''
    title_text = models.CharField(max_length=200)
    desc_text = models.TextField()
    impact_text = models.TextField()
    add_date = models.DateTimeField('date added')
    due_date = models.DateTimeField('complete by')
    priority = models.FloatField()

    def __repr__(self):
        return self.add_date
