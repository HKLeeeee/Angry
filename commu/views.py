from django.shortcuts import render, redirect, get_object_or_404
from commu.models import Board, Comment, Media
from commu.forms import BoardForm, BoardDetailForm


def b_list(request, media_id):

    posts = Board.objects.all().order_by('-id')
    context = {
        "posts": posts
    }
    return render(request, 'commu/list.html', context)


def b_create(request):
    if request.method == 'POST':
        title = request.POST['b_title']
        content = request.POST['b_content']
        user = request.user
        board = Board(
            b_title=title,
            b_content=content,
            b_author=user
        )
        board.save()
        return redirect('commu:b_list')
    else:
        boardForm = BoardForm()
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board
        }
        return render(request, 'commu/create.html', context)


def b_detail(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    comments = post.comment_set.all().order_by('-id')
    context = {
        "detail_form": board_detail_form,
        'comments': comments,
        'post': post
    }
    return render(request, 'commu/detail.html', context)


def b_modify(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == 'POST':
        board.b_title = request.POST['b_title']
        board.b_content = request.POST['b_content']
        board.b_author = request.user
        board.save()
        return redirect('commu:b_list')
    else:
        boardForm = BoardForm
        context = {
            'boardForm': boardForm
        }
        return render(request, 'commu/modify.html', context)
