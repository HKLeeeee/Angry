from django.shortcuts import render


def search(request):
    pass


def result(request):
    return render(request, 'search/results.html')
