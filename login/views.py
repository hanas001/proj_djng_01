from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    html = "<html><body style=\"padding: 50px\">" \
           "<h1>Логин</h1>" \
           "<form method=\"post\">" \
           "<div style=\"margin: 20px 0\">" \
           "<label for =\"uname\"><b>Ваш логин</b></label><br>" \
           "<input type=\"text\" placeholder=\"Email или имя пользователя\" name=\"username\">" \
           "</div>" \
           "<div style=\"margin: 20px 0\">" \
           "<label for=\"psw\"><b>Пароль</b></label><br>" \
           "<input type=\"password\" placeholder=\"Ваш пароль\" name=\"password\">" \
           "</div>" \
           "<button type=\"submit\">Далее</button>" \
           "</form>" \
           "</body></html>"
    return HttpResponse(html)
