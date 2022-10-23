from django.urls import path
from app.olimp.views import \
    StandList, StandDetail, StandCreateView, \
    SportsmanList, SportsmanDetail, SportsmanCreateView, \
    TrenerList, TrenermanDetail, TrenerCreateView, \
    FeedBackCreateView

urlpatterns = [
    # Маршрут ссылки на все записи новостей
    path('', StandList.as_view(), name='stand_list_view'),
    # Маршрут ссылки на конкретную детализированную запись новости
    path('<int:pk>/', StandDetail.as_view(), name='stand_detail_view'),
    # Маршрут ссылки на добавление новости
    path(r'add_stand/', StandCreateView.as_view(), name='add_stand'),

    # Маршрут ссылки на все записи спортсмены
    path('sportsman/', SportsmanList.as_view(), name='sportsman'),
    # Маршрут ссылки на конкретную детализированную запись спортсмена
    path('sportsman/<int:pk>', SportsmanDetail.as_view(), name='sportsman_detail_view'),
    # Маршрут ссылки на добавление спортсмена
    path('sportsman/add_sportsman', SportsmanCreateView.as_view(), name='add_sportsman'),

    # Маршрут ссылки на все записи тренера
    path('trener/', TrenerList.as_view(), name='trener'),
    # Маршрут ссылки на конкретную детализированную запись тренера
    path('trener/<int:pk>', TrenermanDetail.as_view(), name='trener_detail_view'),
    # Маршрут ссылки на добавление тренера
    path('trener/add_trener', TrenerCreateView.as_view(), name='add_trener'),

    # Маршрут ссылки на добавление обратной связи
    path('feedback/', FeedBackCreateView.as_view(), name='feedback'),

]
