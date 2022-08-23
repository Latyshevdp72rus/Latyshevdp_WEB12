from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal
from app.olimp.forms import StandForm
from django.urls import reverse_lazy
from app.olimp.filters import StandFilter


class StandList(FilterView):
    model = Stand
    filterset_class = StandFilter
    context_object_name = "stands"
    template_name = "stand/stand_list.html"
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stands"] = self.queryset
        context["title"] = "Новостной сайт «Олмипийские чемпионы»"
        return context

    def get_queryset(self):
        return Stand.objects.filter(stand_is_visible=False)


class StandDetail(DetailView):
    model = Sportsman
    context_object_name = "sportsman"
    template_name = "stand/stand_detail.html"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context["sportsman"] = self.queryset
        context["title"] = "Биография спортсмена"
        return context


class StandCreateView(CreateView):
    model = Stand
    model_form = StandForm
    context_object_name = "stands"
    template_name = "stand/stand_add.html"
    success_url = reverse_lazy("add_stand")
    fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stands"] = self.queryset
        context["title"] = "Добавления спортсмена на стэнд"
        return context
