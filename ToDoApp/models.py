from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoList(models.Model):
    
    "Details of each ToDo Task"

    Title = models.CharField(primary_key=True,max_length=30)
    Description = models.TextField(blank=True)
    Deadline_Date = models.DateTimeField()
    status_options = [
        ('In Progress','In Progress'),
        ('Completed', 'Completed'),
        ('Pending','Pending')
    ]
    Status = models.CharField(max_length=15,choices=status_options,default="In Progress")
    CreatedAt =  models.DateTimeField(auto_now_add=True)
    ModifiedAt =  models.DateTimeField(auto_now=True)

    def __str__(self):
        "Return human readable string for object ToDoList"
        return (self.Title)