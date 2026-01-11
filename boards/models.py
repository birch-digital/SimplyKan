# Imports
## Django imports
from django.db import models
from django.contrib.auth import get_user_model

# Auth user setup
User = get_user_model()

# Models
## Boards: Contain tasks per project/category; users can have multiple boards
class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


## Tasks: Have state and belong to only one project
class Task(models.Model):
    class State(models.IntegerChoices):
        TODO = 0
        WIP = 1
        DONE = 2

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100)
    task_details = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    state = models.IntegerField(choices=State.choices, default=State.TODO)

    def __str__(self):
        return self.task_title

