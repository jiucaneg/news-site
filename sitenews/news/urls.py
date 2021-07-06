from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = (

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('news/add_news/', CreatePost.as_view(), name='add_news'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
    path('post/<str:slug>/', ViewPost.as_view(), name='post'),
    path('', Home.as_view(), name='home'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="news/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="news/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="news/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="news/password_reset_done.html"),
         name="password_reset_complete"),
)

