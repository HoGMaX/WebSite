from django.urls import path
from . import views as ViewsUser
from django.contrib.auth import views as ViewsAuth

urlpatterns = [
    path('user/', ViewsAuth.LoginView.as_view(template_name = 'users/user.html'),name = "user"),
    path('exit/', ViewsAuth.LogoutView.as_view(template_name = 'users/exit.html'),name = "exit"),
    path('regform/', ViewsUser.regform, name = "regform"),
    path('profile/', ViewsUser.profile, name = "profile"),
]