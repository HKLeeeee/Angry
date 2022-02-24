from django.shortcuts import render,redirect,get_object_or_404
from commu.models import Board,Comment
from commu.forms import BoardForm



def b_list(request):
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        context = {
            "posts": posts
        }
        return render(request,'commu/list.html', context)
    else:
        return redirect('home')


def b_create(request):
    if request.method == 'POST':
        title = request.POST['b_title']
        content = request.POST['b_content']
        user = request.user
        board = Board(
            b_title=title,
            b_content=content,
            user=user,
        )
        board.save()
        return redirect ('')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board
        }
        return render(request,'commu/create.html', context)

