from django.shortcuts import render
from .models import Board

# boards = [
#     {'id': 1, 'name': 'Looking for JavaScript Programmers'},
#     {'id': 2, 'name': 'Seeking Frontend Devs in Austin'},
#     {'id': 3, 'name': 'Any Python Developers?'},
# ]

def home(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'base/home.html', context)

def board(request, pk):
    board = Board.objects.get(id=pk)
    context = {'board': board}
    return render(request, 'base/board.html', context)
