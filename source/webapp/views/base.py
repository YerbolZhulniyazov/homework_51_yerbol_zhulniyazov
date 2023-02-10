from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.cat import Cat


def index_view(request: WSGIRequest):
    cat_status = Cat.get_status()
    if cat_status:
        context = {'cat_message': 'Желаем приятной игры с вашим котом'}
    else:
        context = {'cat_message': 'Какая жалость, ваш питомец скончался, чтобы'
                                       ' продолжить игру создайте нового кота'}
    return render(request, 'index.html', context=context)