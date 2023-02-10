from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from webapp.cat import Cat


def cat_view(request: WSGIRequest):
    action_form = request.POST.get('action')
    message = Cat.action(action_form)
    Cat.name = request.POST.get('name', Cat.name)
    cat_status = Cat.get_status()
    if cat_status:
        context = {
            'name': Cat.name,
            'image': Cat.image,
            'age': Cat.age,
            'happiness': Cat.happiness,
            'satiety': Cat.satiety,
            'message': message
        }
        return render(request, 'cat.html', context=context)
    else:
        response = redirect('/')
        return response
