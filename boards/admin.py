from django.contrib import admin
from .models import Board, Task

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'description')
    list_filter = ('owner',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'board', 'state', 'timestamp')
    list_filter = ('board', 'state')