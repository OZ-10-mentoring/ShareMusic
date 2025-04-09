from django.contrib import admin
from django.urls import path

from board.views import (
    home,
    get_posts,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('board/<str:board_name>', get_posts, name='get_boards'),
]
