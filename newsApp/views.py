from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='2c0d32cdf79b4f7eb97b3f4b10b8b5d4')
    headLines = newsApi.get_top_headlines(sources='ign, cnn')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "main/index.html", context={"mylist": mylist})