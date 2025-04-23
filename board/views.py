from django.http import Http404
from django.shortcuts import render, redirect

from board.models import Post


def home(request):
    post_qs = Post.objects.values("genre").distinct()
    return render(
        request,
        "home.html",
        {
            'post_qs': post_qs,
        }
    )


def get_posts(request, board_name):
    # Selcet * from board_post
    korea_board_name = "게시판"
    if board_name == "recommend":
        korea_board_name = "recommend"
        post_qs = Post.objects.filter(classification__in=["추천", "추천게시판", "recommend"])
    elif board_name == "review":
        korea_board_name = "review"
        post_qs = Post.objects.filter(classification__in=["리뷰", "리뷰게시판", "review"])
    elif board_name == "free":
        korea_board_name = "free"
        post_qs = Post.objects.filter(classification__in=["자유", "자유게시판", "free"])

    return render(
        request,
        "board.html",
        {
            "posts": post_qs,
            "korea_board_name": korea_board_name,
            "board_name": board_name,
        }
    )


def get_post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(
            request,
            "404.html",
            {}
        )
    return render(
        request,
        "post.html",
        {
            "post": post,
        }
    )


def update_post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(
            request,
            "404.html",
            {}
        )
    return render(
        request,
        "write.html",
        {
            "korea_board_name": post.classification,
            "board_name": post.classification,
            "post": post,
            "action": "update",
        },
    )


def create_post(request):
    board_name = request.GET.get('type')
    korea_board_name = "board"
    if board_name == "recommend":
        korea_board_name = "recommend"
    elif board_name == "review":
        korea_board_name = "review"
    elif board_name == "free":
        korea_board_name = "free"
    if request.method == "GET":
        return render(
            request,
            "write.html",
            {
                "korea_board_name": korea_board_name,
                "board_name": board_name,
            },
        )
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content2')
        music_link = request.POST.get('music_link')
        genre = request.POST.get('genre')
        board_name = request.POST.get('board_name')
        if board_name == "recommend":
            korea_board_name = "recommend"
        elif board_name == "review":
            korea_board_name = "review"
        elif board_name == "free":
            korea_board_name = "free"
        Post.objects.create(
            title=title,
            content=content,
            classification=korea_board_name,
            music_link=music_link,
            genre=genre,
        )
        return redirect('get_boards', board_name=board_name)


def get_genre_posts(request):
    genre = request.GET.get("genre")
    post_qs = Post.objects.filter(genre=genre)
    return render(
        request,
        "board.html",
        {
            "posts": post_qs,
            "genre": genre
        }
    )