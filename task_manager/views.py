from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse('Hello, World! 12 2023')


class IndexView(TemplateView):
    template_name = "index.html"