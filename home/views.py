from django.shortcuts import render


def index(request):
    """ A view to view the index page """

    return render(request, 'home/index.html')
