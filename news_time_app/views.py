from django.shortcuts import render
from newsapi import NewsApiClient

#Views 
def index(request):
    
    newsapi = NewsApiClient(api_key='a7dd72a8e05c40c1af55d568704dd140')
    top_headlines = newsapi.get_top_headlines(sources="google-news-in")

    toplines = top_headlines['articles']
    desc = [] # description list
    news = [] # news list
    img = [] # image list

    for i in range(len(toplines)):
        jsondata = toplines[i]
        news.append(jsondata['title'])
        desc.append(jsondata['description'])
        img.append(jsondata['urlToImage'])
    headlines_data = zip(news,desc,img)
    
    return render(request, 'news/index.html',context={"headlines_data": headlines_data})