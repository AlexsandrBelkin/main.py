from django.shortcuts import render, redirect
from news.models import News, User

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

def homework(request):
    return render(request, "news/homework.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = User.objects.get(user_name=username)
        password_bd = user.password
        if password_bd == password:
            pass
        else:
            return render(request, "news/login.html")
    else:
        return render(request, "news/login.html")

def registr(request):
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get("firstname")
        user.last_name = request.POST.get("secondname")
        user.user_name = request.POST.get("username")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.password = request.POST.get("password")
        user.save()
        return redirect("/post/authorization")
    else:
        return render(request, "news/registr.html")

def classwork(request):
    return render(request, "news/classwork.html")