from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .forms import NewUserForm
from .models import ShortUrlModel

# Получаем  ID последней записи в модели ShortUrlModel
CHAR = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
base = len(CHAR)

BASE_URL = 'http://127.0.0.1:8000/sh/'


def main(request):
    """
    Рендер шаблона главной страницы

    """
    return render(request, 'main_page.html')


def new_user(request):
    """
    Создание нового пользователя

    """
    if request.method == 'POST':
        user = NewUserForm(request.POST)
        if user.is_valid():
            new_user = User.objects.create_user(**user.cleaned_data)
            return redirect('main_app:main')
    else:
        form = NewUserForm()
        context = {'form': form}
        return render(request, 'registration.html', context)


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main_app:main')


class Logout(LogoutView):
    next_page = "main_app:main"


def coding(id):
    """

    Возвращает уникальный ключ, который добавляется к BASE_URL для
    получения нового короткого URL
    """
    ret = []
    while id > 0:
        val = id % base
        ret.append(CHAR[val])
        id = id // base
    return "".join(ret[::-1])

def decoding(slug):
    res = []
    for i in slug:
        for ind, it in enumerate(CHAR):
            if i == it:
                res.append(ind)
            else:
                continue
    return sum(res)+1

def short_url_creater(request):
    """
    Создает новый уникальный URL.
    Для авторизованных пользователей сохраняет созданные ими которкие URL в таблицу ShortUrlModel с привязкой к пользователю
    Для анонимных сохраняет созданные ими которкие URL в таблицу привязывая запись к учётной записи admina
    """
    if request.method == 'POST':
        ID = ShortUrlModel.objects.last()
        if ID != None:
            ID = ID.id
        else:
            ID = 1
        if request.user.is_authenticated:
            new_short_url = f'{BASE_URL}' + coding(ID)
            object_for_save = ShortUrlModel(user=User.objects.get(id=request.user.id), long_url=request.POST['url'],
                                            short_url=new_short_url)
            object_for_save.save()
            print('CREATED')
            return render(request, 'short_url_ok.html', context={'url': new_short_url})
        else:
            try:
                new_short_url = f'{BASE_URL}' + coding(ID)
                object_for_save = ShortUrlModel(user=User.objects.get(username='admin'), long_url=request.POST['url'],
                                                short_url=new_short_url)
                object_for_save.save()
                print('CREATED')
                return render(request, 'short_url_ok.html', context={'url': new_short_url})
            except Exception:
                return HttpResponse('Создайте суперпользователя >>> py manage.py createsuperuser')
    else:
        return render(request, 'short.html')


def all_created_short_url(request, id):
    list_of_url = ShortUrlModel.objects.filter(user=id)
    if len(list_of_url) == 0:
        return render(request, 'detail.html', context={'list': 'Ничего не создано'})
    return render(request, 'detail.html', context={'list': list_of_url})

def redir_to_long_url(request, slug):
    get_id_long_url = decoding(slug)
    get_objects_for_extr_long_url = ShortUrlModel.objects.get(id=get_id_long_url)
    long_url = get_objects_for_extr_long_url.long_url
    return redirect(long_url)