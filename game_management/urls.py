from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'game_management'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view()),
    path('accounts/logout-then-login/', auth_views.logout_then_login),
    path('schedule', views.schedule, name='schedule'),
    path('members', views.members, name='members'),
    path('masters', views.masters, name='masters'),
    path('results', views.results, name='results'),
    path('rating', views.rating, name='rating'),
    path('promo', views.promo, name='promo'),
    path('bot', views.bot, name='bot'),
]


