
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article
from random import randint

def home_view(request):
    random_id = randint(1, 3)
    print(f"randint: {random_id}")
    article_obj = Article.objects.get(id=random_id)
    article_qs = Article.objects.all()

    context = {
        "object_list": article_qs,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
    }

    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)