from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="제목",
    )
    content = models.TextField(
        help_text="내용",
    )
    classification = models.CharField(
        max_length=100,
        help_text="분류",
        default="free",
    )
    music_link = models.CharField(
        max_length=1024,
        help_text="음악 링크",
        null=True,
        blank=True,
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="삭제여부",
    )
    genre = models.CharField(
        max_length=10,
        help_text="장르",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title


class PostSummary(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.DO_NOTHING,
    )
    content = models.TextField(
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
