from django.http import HttpResponse
from django.shortcuts import render
from news.models import News

def test(request):
    #return HttpResponse("<h1>Hello world!</h1>")
    return render(request, "news/test.html")

def test_news(request):
    news = News.objects.all()
    # response = ""
    # for item in news:
    #     item_str = "<p>" + item.title + str(item.created_at) + str(item.is_published) + "</p>"
    #     response += item_str + "\n"
    # return HttpResponse(response)
    return render(request, "news/test_news.html", context={"news": news})

def task(request):
    return render(request, "news/task.html")
