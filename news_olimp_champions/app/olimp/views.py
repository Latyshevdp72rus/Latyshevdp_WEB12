from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal, FeedBack
from app.olimp.forms import StandForm, SportsmanForm, TrenerForm, ClubForm,FeedBackForm
from django.urls import reverse_lazy
from app.olimp.filters import StandFilter, SportsmanFilter, TrenerFilter


###########################################################
class StandList(FilterView):
    model = Stand
    filterset_class = StandFilter
    context_object_name = "stands"
    template_name = "stand/stand_list.html"
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stands"] = self.queryset
        context["title"] = "Новости"
        return context

    def get_queryset(self):
        return Stand.objects.filter(stand_is_visible=False)


class StandDetail(DetailView):
    model = Stand
    context_object_name = "stands"
    template_name = "stand/stand_detail.html"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context["stands"] = self.queryset
        context["title"] = "Новости"
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
        context["title"] = "Добавить новость"
        return context


###########################################################
class SportsmanList(FilterView):
    model = Sportsman
    filterset_class = SportsmanFilter
    context_object_name = "sportsmans"
    template_name = "sportsman/sportsman_list.html"
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sportsmans"] = self.queryset
        context["title"] = "Спортсмены"
        return context

    def get_queryset(self):
        return Sportsman.objects.filter(sportsman_is_visible=False)


class SportsmanDetail(DetailView):
    model = Sportsman
    context_object_name = "sportsman"
    template_name = "sportsman/sportsman_detail.html"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context["sportsman"] = self.queryset
        context["title"] = "Новости"
        return context


class SportsmanCreateView(CreateView):
    model = Sportsman
    model_form = SportsmanForm
    context_object_name = "sportsmans"
    template_name = "sportsman/sportsman_add.html"
    success_url = reverse_lazy("add_sportsman")
    fields = ["sportsman_name", "sportsman_country", "sportsman_birthday", "sportsman_biogrpahy", "view_sports_id",
              "trener_id", "sportsman_img", ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sportsman"] = self.queryset
        context["title"] = "Добавить спортсмена"
        return context


###########################################################
class TrenerList(FilterView):
    model = Trener
    filterset_class = TrenerFilter
    context_object_name = "treners"
    template_name = "trener/trener_list.html"
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["treners"] = self.queryset
        context["title"] = "Тренеры"
        return context

    def get_queryset(self):
        return Trener.objects.filter(trener_is_visible=False)


class TrenermanDetail(DetailView):
    model = Trener
    context_object_name = "trener"
    template_name = "trener/trener_detail.html"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context["trener"] = self.queryset
        context["title"] = "Новости"
        return context


class TrenerCreateView(CreateView):
    model = Trener
    model_form = TrenerForm
    context_object_name = "treners"
    template_name = "trener/trener_add.html"
    success_url = reverse_lazy("add_trener")
    fields = ["trener_name", "club_id", "trener_img"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["treners"] = self.queryset
        context["title"] = "Добавить тренера"
        return context


#
class ClubCreateView(CreateView):
    model = Club
    model_form = ClubForm
    context_object_name = "clubs"
    template_name = "club/club_add.html"
    success_url = reverse_lazy("add_club")
    fields = ["club_name", "club_img"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = self.queryset
        context["title"] = "Добавить клуб"
        return context


#

class FeedBackCreateView(CreateView):
    model = FeedBack
    model_form = FeedBackForm
    context_object_name = "feedback"
    template_name = "feedback/feedback_msg.html"
    success_url = reverse_lazy("feedback")
    fields = ["fb_name", "fb_email", "fb_message", "fb_img",]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feedback"] = self.queryset
        context["title"] = "Обратная связь"
        return context
