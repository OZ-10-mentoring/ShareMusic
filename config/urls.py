from django.contrib import admin
from django.urls import path

from board.views import (
    create_post,
    home,
    get_posts,
    get_genre_posts
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('board/<str:board_name>', get_posts, name='get_boards'),
    path('board/post/write', create_post, name='create_post'),
    path('board/genre/', get_genre_posts, name='get_genre_posts')
]
