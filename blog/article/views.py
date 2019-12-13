from django.shortcuts import render
from article.models import Article, Comment

def article(request):
    '''
    Render the article page
    '''
    articles = {article:Comment.objects.filter(article=article) for article in Article.objects.all()}
    context = {'articles':articles}
    return render(request, 'article/article.html', context)
