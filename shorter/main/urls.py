
from django.urls import path

from .views import main, new_user, Login, Logout, short_url_creater, all_created_short_url, redir_to_long_url

app_name = 'main_app'
urlpatterns = [
    path('', main, name='main'),
    path('sh/<slug:slug>', redir_to_long_url, name='url_redir'),
    path('reg/', new_user, name='reg'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('short/', short_url_creater, name='short'),
    path('created/<int:id>', all_created_short_url, name='created'),
]
