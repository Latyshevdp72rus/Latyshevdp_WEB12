from django.urls import path
from app.user.views import create_user, login_user, user_logout

urlpatterns = [
    # Регистрация представления на регистрационной форме
    path("registration/", create_user, name="register"),
    # Регистрация представления на логиинование
    path("login/", login_user, name="login"),
    # Регистрация представления на разлогинивания
    path("logout/", user_logout, name="logout"),
]
