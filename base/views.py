from django.shortcuts import render
from .models import Board

boards = [
    {'id': '1b1e182a-b265-4ebe-bd01-2fd465829c89', 'name': 'Looking for JavaScript Programmers'},
    {'id': '240cc256-cd75-42f1-ae03-6096446e5583', 'name': 'Seeking Frontend Devs in Austin'},
    {'id': '69707184-2fd3-4ecf-84b8-b16c06c3aedf', 'name': 'Any Python Developers?'},
]

def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'base/home.html', context)

def board(request, pk):
    board = None
    for post in boards:
        if post['id'] == str(pk):
           board = post
    
    context = {'board': board}
    return render(request, 'base/board.html', context)
