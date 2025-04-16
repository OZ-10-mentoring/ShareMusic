from django.shortcuts import render, redirect

from board.models import Post


def home(request):
    return render(
        request,
        "home.html",
    )


def get_posts(request, board_name):
    # Selcet * from board_post
    korea_board_name = "게시판"
    if board_name == "recommend":
        korea_board_name = "추천"
        post_qs = Post.objects.filter(classification__in=["추천", "추천게시판"])
    elif board_name == "review":
        korea_board_name = "리뷰"
        post_qs = Post.objects.filter(classification__in=["리뷰", "리뷰게시판"])
    elif board_name == "free":
        korea_board_name = "자유"
        post_qs = Post.objects.filter(classification__in=["자유", "자유게시판"])

    return render(
        request,
        "board.html",
        {
            "posts": post_qs,
            "korea_board_name": korea_board_name,
            "board_name": board_name,
        }
    )


def create_post(request):
    board_name = request.GET.get('type')
    korea_board_name = "게시판"
    if board_name == "recommend":
        korea_board_name = "추천"
    elif board_name == "review":
        korea_board_name = "리뷰"
    elif board_name == "free":
        korea_board_name = "자유"
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
            korea_board_name = "추천"
        elif board_name == "review":
            korea_board_name = "리뷰"
        elif board_name == "free":
            korea_board_name = "자유"
        Post.objects.create(
            title=title,
            content=content,
            classification=korea_board_name,
            music_link=music_link,
            genre=genre,
        )
        return redirect('get_boards', board_name=board_name)
