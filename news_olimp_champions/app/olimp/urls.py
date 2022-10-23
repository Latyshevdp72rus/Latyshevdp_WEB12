from django.urls import path
from app.olimp.views import \
    StandList, StandDetail, StandCreateView, \
    SportsmanList, SportsmanDetail, SportsmanCreateView, \
    TrenerList, TrenermanDetail, TrenerCreateView, \
    FeedBackCreateView

urlpatterns = [
    # Регистрация представления на все записи новостей
    path('', StandList.as_view(), name='stand_list_view'),
    # Регистрация представления на конкретную детализированную запись новости
    path('<int:pk>/', StandDetail.as_view(), name='stand_detail_view'),
    # Регистрация представления на добавление новости
    path(r'add_stand/', StandCreateView.as_view(), name='add_stand'),

    # Регистрация представления на все записи спортсмены
    path('sportsman/', SportsmanList.as_view(), name='sportsman'),
    # Регистрация представления на конкретную детализированную запись спортсмена
    path('sportsman/<int:pk>', SportsmanDetail.as_view(), name='sportsman_detail_view'),
    # Регистрация представления на добавление спортсмена
    path('sportsman/add_sportsman', SportsmanCreateView.as_view(), name='add_sportsman'),

    # Регистрация представления на все записи тренера
    path('trener/', TrenerList.as_view(), name='trener'),
    # Регистрация представления на конкретную детализированную запись тренера
    path('trener/<int:pk>', TrenermanDetail.as_view(), name='trener_detail_view'),
    # Регистрация представления на добавление тренера
    path('trener/add_trener', TrenerCreateView.as_view(), name='add_trener'),

    # Регистрация представления на добавление обратной связи
    path('feedback/', FeedBackCreateView.as_view(), name='feedback'),
]