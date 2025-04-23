from django.contrib import admin
from django.urls import path

from board.views import (
    create_post,
    delete_post,
    home,
    get_posts,
    get_post_detail,
    get_genre_posts,
    update_post_action,
    update_post_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('board/<str:board_name>', get_posts, name='get_boards'),
    path('board/post/write', create_post, name='create_post'),
    path('board/genre/', get_genre_posts, name='get_genre_posts'),
    path('post/<int:post_id>', get_post_detail, name='get_post_detail'),
    path('post/<int:post_id>/update', update_post_view, name='update_post_view'),
    path('post/<int:post_id>/update/action', update_post_action, name='update_post_action'),
    path('post/<int:post_id>/delete', delete_post, name='delete_post')
]
