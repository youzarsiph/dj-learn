""" Views """

from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Index view"""

    return HttpResponse("Hello from dj-learn")
