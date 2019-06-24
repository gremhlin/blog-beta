from django.shortcuts import render

def post_list(request):
    return render(request, 'journal/post_list.html', {})
