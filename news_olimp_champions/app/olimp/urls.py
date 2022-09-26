from django.urls import path
from app.olimp.views import \
    StandList, StandDetail, StandCreateView, \
    SportsmanList, SportsmanDetail, SportsmanCreateView, \
    TrenerList, TrenermanDetail, TrenerCreateView, \
    FeedBackCreateView

urlpatterns = [
    path('', StandList.as_view(), name='stand_list_view'),
    path('<int:pk>/', StandDetail.as_view(), name='stand_detail_view'),
    path(r'add_stand/', StandCreateView.as_view(), name='add_stand'),

    path('sportsman/', SportsmanList.as_view(), name='sportsman'),
    path('sportsman/<int:pk>', SportsmanDetail.as_view(), name='sportsman_detail_view'),
    path('sportsman/add_sportsman', SportsmanCreateView.as_view(), name='add_sportsman'),

    path('trener/', TrenerList.as_view(), name='trener'),
    path('trener/<int:pk>', TrenermanDetail.as_view(), name='trener_detail_view'),
    path('trener/add_trener', TrenerCreateView.as_view(), name='add_trener'),

    path('feedback/', FeedBackCreateView.as_view(), name='feedback'),

]
