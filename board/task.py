from celery import shared_task

from board.models import PostSummary
from common.utils import generate_ai_summary

from config.celery import app


@shared_task
def add(x, y):
    return x + y


@app.task(time_limit=30)
def async_generate_post_summary(post_id, title, content):
    PostSummary.objects.create(
        post_id=post_id,
        content=generate_ai_summary(
            title,
            content,
        )
    )
