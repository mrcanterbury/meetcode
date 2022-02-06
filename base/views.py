from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Board, Category, Message
from .forms import BoardForm






def userLogin(request):
    page = 'user-login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('user-error')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('user-error')
        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def userLogout(request):
    logout(request)
    return redirect('home')


def userRegister(request):
    page = 'user-register'
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return redirect('user-error')
    
    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)


def home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    
    board_list = Board.objects.filter(
        Q(name__icontains=query) |
        Q(city__icontains=query) |
        Q(category__name__icontains=query)
    )
    
    board_count = board_list.count()
    activity_comments = Message.objects.filter(Q(board__city__icontains=query))[:10]
    categories = Category.objects.all()[:10]
    cities = Board.objects.all()[:10]
    
    context = {'board_list': board_list, 'board_count': board_count,
               'activity_comments': activity_comments, 'categories': categories, 'cities': cities}
    return render(request, 'base/home.html', context)


def board(request, pk):
    board = Board.objects.get(id=pk)
    comments = board.message_set.all().order_by('-created')
    members = board.members.all()[:20]
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            board = board,
            body = request.POST.get('body')
        )
        board.members.add(request.user)
        return redirect('board', pk=board.id)
    
    context = {'board': board, 'comments': comments, 'members': members}
    return render(request, 'base/board.html', context)


@login_required(login_url='user-login')
def newBoard(request):
    form = BoardForm
    
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/new_board.html', context)


@login_required(login_url='user-login')
def editBoard(request, pk):
    board = Board.objects.get(id=pk)
    form = BoardForm(instance = board)
    
    if request.user != board.author:
        return redirect('user-error')
    
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'base/edit_board.html', context)


@login_required(login_url='user-login')
def deleteBoard(request, pk):
    board = Board.objects.get(id=pk)
    
    if request.method == 'POST':
        board.delete()
        return redirect('home')
        
    return render(request, 'base/delete_board.html', {'obj': board})

@login_required(login_url='user-login')
def deleteComment(request, pk):
    comment = Message.objects.get(id=pk)
    parentBoard = comment.board.id
    
    if request.user != comment.user:
        return redirect('user-error')
    
    if request.method == 'POST':
        comment.delete()
        return redirect('board', pk=parentBoard)
        
    return render(request, 'base/delete_comment.html', {'obj': comment})

def userError(request):
    return render(request, 'base/error.html')
    