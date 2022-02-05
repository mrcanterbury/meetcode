from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Board, Category
from .forms import BoardForm

def home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    
    boards = Board.objects.filter(
        Q(name__icontains=query) |
        Q(city__icontains=query) |
        Q(category__name__icontains=query)
    )
    
    categories = Category.objects.all()[:10]
    cities = Board.objects.all()[:10]
    
    context = {'boards': boards, 'categories': categories, 'cities': cities}
    return render(request, 'base/home.html', context)


def board(request, pk):
    board = Board.objects.get(id=pk)
    context = {'board': board}
    return render(request, 'base/board.html', context)


def newBoard(request):
    form = BoardForm
    
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/new_board.html', context)


def editBoard(request, pk):
    board = Board.objects.get(id=pk)
    form = BoardForm(instance = board)
    
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/edit_board.html', context)


def removeBoard(request, pk):
    board = Board.objects.get(id=pk)
    
    if request.method == 'POST':
        board.delete()
        return redirect('home')
        
    return render(request, 'base/remove.html', {'obj': board})
    