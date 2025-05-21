from django.contrib import admin

from board.models import Post, PostSummary


admin.site.register(Post)
admin.site.register(PostSummary)
