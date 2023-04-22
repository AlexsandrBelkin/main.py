from django.urls import path
from news.views import test, test_news, task, homework, login, registr, classwork

app_name = "news"

urlpatterns = [
    path("news/", test, name="news"),
    path("list/", test_news, name="list"),
    path("task/", task, name="task"),
    path("homework/", homework, name="homework"),
    path("register/", registr, name="register"),
    path("authorization/", login, name="authorization"),
    path("classwork/", classwork, name="classwork")
]