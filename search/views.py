from django.shortcuts import render, redirect, reverse


def search(request):
    # post로 넘어온 options 이랑 search 받고
    option = request.POST['option']
    keyword = request.POST['keyword']
    # GET으로 넘겨줌
    return redirect(reverse('search:result')+"?option="+option+"&keyword="+keyword)


def result(request):
    return render(request, 'search/search_results.html')
