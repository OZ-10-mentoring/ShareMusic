from django.shortcuts import render

from board.models import Post
from customer.models import Customer


def set_customer_with_cookie(request):
    username = request.POST.get('username')
    post_qs = Post.objects.values("genre").distinct()
    rendering = render(
        request,
        "home.html",
        {
            'post_qs': post_qs,
        }
    )
    customer, _ = Customer.objects.get_or_create(nickname=username)
    rendering.set_cookie('customer_id', str(customer.id))
    return rendering
