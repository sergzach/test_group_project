from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from .models import Post, Group
from yatube.settings import PAGE_NUMBER

user = get_user_model()


def index(request):
    content = Post.objects.select_related('group')
    paginator = Paginator(content, PAGE_NUMBER)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'paginator': paginator}
    return render(request, 'index.html', context)
