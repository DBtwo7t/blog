from django.shortcuts import render

def article(request):
    '''
    Render the article page
    '''
    return render(request, 'article/article.html')
