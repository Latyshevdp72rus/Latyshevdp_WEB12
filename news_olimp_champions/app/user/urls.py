from django.urls import path
from app.user.views import create_user, login_user, user_logout

urlpatterns = [
    path('registration/', create_user, name="register"),
    path('login/', login_user, name='login'),
    path('logout/', user_logout, name='logout'),

]
