import json

from django.shortcuts import render, redirect, get_object_or_404, reverse
from commu.models import Board, Comment, Media
from commu.forms import BoardForm, BoardDetailForm
from django.http import JsonResponse
from django.http import HttpResponse


def b_list(request, media_id, category):
    if not Media.objects.filter(pk=media_id).exists():
        # media_id가  meda tabel에 없을때
        media_title = request.GET['title']
        # 새로운 레코드 생성
        new_media = Media(id=media_id, title=media_title)
        new_media.save()

    media = Media.objects.get(id=media_id)
    # media_id가 일치하는 post들을 다 가져옴
    posts = media.board_set.all().order_by('-id')

    context = {
        "posts": posts,
        "media_id": media_id,
        "category": category
    }

    return render(request, 'commu/list.html', context)


def b_create(request, media_id, category):
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
        return redirect('commu:b_list', media_id, category)
    else:
        boardForm = BoardForm()
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'media_id': media_id,
            'category': category
        }
        return render(request, 'commu/create.html', context)


def b_detail(request, board_id, media_id, category):
    post = get_object_or_404(Board, pk=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    comments = post.comment_set.all().order_by('-id')
    context = {
        "detail_form": board_detail_form,
        'comments': comments,
        'post': post,
        'category': category,
        'media_id': media_id

    }
    return render(request, 'commu/detail.html', context)


def b_modify(request, board_id, media_id, category):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        board.b_title = request.POST['b_title']
        board.b_content = request.POST['b_content']

        board.b_author = request.user
        board.save()
        return redirect('commu:b_list', media_id, category)
    else:
        boardForm = BoardForm(instance=board)
        context = {
            'boardForm': boardForm,
            'board': board,
            'category': category
        }
        return render(request, 'commu/modify.html', context)


def b_delete(request, board_id, media_id, category):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('commu:b_list', media_id, category)


def create_comment(request, media_id, category, board_id):
    comment = Comment()
    comment.c_author = request.user
    comment.c_content = request.GET['comment_content']
    comment.c_board_id = request.GET['c_board_id']

    comment.save()

    return JsonResponse({
        'c_id': comment.c_board_id,
        'c_author': comment.c_author,
        'c_content': comment.c_content
    }, json_dumps_params={'ensure_ascii': True})


def b_like(request):
    if request.is_ajax():
        post_id = request.GET['post_id']
        post = Board.objects.get(id=post_id)

        if not request.user.is_authenticated:
            message = "로그인을 해주세요"  # 화면에 띄울 메세지
            context = {
                "b_like_count": post.b_like.count(),
                'message': message
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user  # 로그인 한 유저
        if post.b_like.filter(id=user.id).exists():  # 이미 좋아요를 누른 유저일떄
            post.b_like.remove(user)
            message = "좋아요 취소"  # 화면에 띄울 메세지
        else:  # 좋아요를 누르지 않은 유저의 경우
            post.b_like.add(user)
            message = "좋아요"

        context = {
            'b_like_count': post.b_like.count(),
            'message': message
        }
        return HttpResponse(json.dumps(context), content_type='application/json')


def comment_Delete(request):
    comment = get_object_or_404(Comment, pk=request.GET['comment_id'])
    comment.delete()
    return JsonResponse({}, json_dumps_params={'ensure_ascii': True})
