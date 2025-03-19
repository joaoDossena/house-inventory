
from django.http import HttpResponse

from articles.models import Article

def home_view(request):
    
    name = "poggers"
    HTML_STRING = f"""<h1>Hello {name}!</h1>"""

    return HttpResponse(HTML_STRING)