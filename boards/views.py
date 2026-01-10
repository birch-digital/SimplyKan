# IMPORTS
## Django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

## Apps
from .models import Board

# VIEWS
##
@login_required
def dashboard(request):
    boards = Board.objects.filter(owner=request.user).order_by('title')
    return render(request, 'boards/dashboard.html', {'boards': boards})


