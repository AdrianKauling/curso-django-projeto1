from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('That\'s my first view with django')


def contact(request):
    return HttpResponse('contact')


def about(request):
    return HttpResponse('About')
