from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal
from app.olimp.forms import StandForm
from django.urls import reverse_lazy


# from app.books.filters import BookFilter
# from app.books.validators import validation_book_name

class StandList(FilterView):
    model = Stand
    # filterset_class = StandFilter
    context_object_name = "stands"
    template_name = "stand/stand_list.html"
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stands"] = self.queryset
        context["title"] = "СТЭНД"
        return context


class StandDetail(DetailView):
    model = Stand
    context_object_name = "stands"
    template_name = "stand/stand_detail.html"
    pk_url_kwarg = "pk"


class StandCreateView(CreateView):
    model = Stand
    model_form = StandForm
    template_name = "stand/add_stand.html"
    success_url = reverse_lazy("add_stand")
    fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event"]
