from django.shortcuts import render

boards = [
    {'id': 1, 'name': 'Looking for JavaScript Programmers'},
    {'id': 2, 'name': 'Seeking Frontend Devs in Austin'},
    {'id': 3, 'name': 'Any Python Developers?'},
]

def home(request):
    context = {'boards': boards}
    return render(request, 'base/home.html', context)

def board(request, pk):
    board = None
    for i in boards:
        if i['id'] == int(pk):
            board = i
    
    context = {'board': board}
    return render(request, 'base/board.html', context)
