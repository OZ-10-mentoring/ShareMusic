from django.shortcuts import render

from board.models import Post


def home(request):
    return render(
        request,
        "home.html",
    )


def get_posts(request, board_name):
    # Selcet * from board_post;
    korea_board_name = "게시판"
    if board_name == "recommend":
        korea_board_name = "추천"
        post_qs = Post.objects.filter(classification="추천게시판")
    elif board_name == "review":
        korea_board_name = "리뷰"
        post_qs = Post.objects.filter(classification="리뷰게시판")
    elif board_name == "free":
        korea_board_name = "자유"
        post_qs = Post.objects.filter(classification="자유게시판")

    return render(
        request,
        "board.html",
        {
            "posts": post_qs,
            "korea_board_name": korea_board_name,
        }
    )
