from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Board, Category
from .forms import BoardForm




def loginRegister(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist.')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Username or password incorrect.')
        
    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    
    board_list = Board.objects.filter(
        Q(name__icontains=query) |
        Q(city__icontains=query) |
        Q(category__name__icontains=query)
    )
    
    board_count = board_list.count()
    
    categories = Category.objects.all()[:10]
    cities = Board.objects.all()[:10]
    
    context = {'board_list': board_list, 'board_count': board_count, 'categories': categories, 'cities': cities}
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
    