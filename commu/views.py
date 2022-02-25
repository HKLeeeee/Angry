from django.shortcuts import render, redirect, get_object_or_404
from commu.models import Board, Comment, Media
from commu.forms import BoardForm, BoardDetailForm


def b_list(request, media_id):
    if not Media.objects.filter(pk=media_id).exists():
        # media_id가  meda tabel에 없을때
        # 새로운 레코드 생성
        media_title = request.GET['title']
        print(media_title)
        new_media = Media(id=media_id, title=media_title)
        new_media.save()

    media = Media.objects.get(id=media_id)
    # media_id가 일치하는 post들을 다 가져옴
    posts = media.board_set.all().order_by('-id')

    context = {
        "posts": posts,
        "media_id": media_id
    }

    return render(request, 'commu/list.html', context)


def b_create(request, media_id):
    if request.method == 'POST':
        title = request.POST['b_title']
        content = request.POST['b_content']
        user = request.user
        board = Board(
            b_title=title,
            b_content=content,
            b_author=user,
            media_id=media_id
        )
        board.save()
        return redirect('commu:b_list', media_id)
    else:
        boardForm = BoardForm()
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'media_id': media_id
        }
        return render(request, 'commu/create.html', context)


def b_detail(request, board_id,media_id):
    post = get_object_or_404(Board, pk=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    comments = post.comment_set.all().order_by('-id')
    context = {
        "detail_form": board_detail_form,
        'comments': comments,
        'post': post
    }
    return render(request, 'commu/detail.html', context)


def b_modify(request, board_id, media_id):

    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        board.b_title = request.POST['b_title']
        board.b_content = request.POST['b_content']

        board.b_author = request.user
        board.save()
        return redirect('commu:b_list', media_id)
    else:
        boardForm = BoardForm(instance=board)
        context = {
            'boardForm': boardForm,
            'board':board
        }
        return render(request, 'commu/modify.html', context)


def b_delete(request,board_id):
    board =get_object_or_404(Board,pk=board_id)
    board.delete()
    return redirect('commu:b_list')





