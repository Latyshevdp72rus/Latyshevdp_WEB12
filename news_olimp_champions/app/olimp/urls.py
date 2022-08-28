from django.urls import path
from app.olimp.views import StandList, StandDetail, StandCreateView,SportsmanList,SportsmanCreateView

urlpatterns = [
    path('', StandList.as_view(), name='stand_list_view'),
    path('<int:pk>', StandDetail.as_view(), name='stand_detail_view'),
    path(r'add_stand/', StandCreateView.as_view(), name='add_stand'),
    path('sportsman/', SportsmanList.as_view(), name='sportsman'),
    path('sportsman/add_sportsman', SportsmanCreateView.as_view(), name='add_sportsman'),

]
