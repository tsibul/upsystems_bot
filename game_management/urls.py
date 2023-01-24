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
    path('glossary', views.glossary, name='glossary'),
    path('bot', views.bot, name='bot'),

    path('glossary/games', views.games, name='games'),
    path('glossary/games/update_game', views.update_game, name='update_game'),
    path('glossary/games/delete_game', views.delete_game, name='delete_game'),

    path('glossary/game_result', views.game_result, name='game_result'),
    path('glossary/game_result/update_result', views.update_result, name='update_result'),
    path('glossary/game_result/delete_result', views.delete_result, name='delete_result'),

    path('glossary/role', views.role, name='role'),
    path('glossary/role/update_role', views.update_role, name='update_role'),
    path('glossary/role/delete_role', views.delete_role, name='delete_role'),

    path('glossary/member_result', views.member_result, name='member_result'),
    path('glossary/member_result/update_member_result', views.update_member_result, name='update_member_result'),
    path('glossary/member_result/delete_member_result', views.delete_member_result, name='delete_member_result'),

    path('glossary/game_functions', views.game_functions, name='game_functions'),
    path('glossary/game_functions/update_function', views.update_function, name='update_function'),
    path('glossary/game_functions/delete_function', views.delete_function, name='delete_function'),

    path('location', views.location, name='location'),
    path('location/update_location', views.update_location, name='update_location'),
    path('location/delete_location', views.delete_location, name='delete_location'),
]


