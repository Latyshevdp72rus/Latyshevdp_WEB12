from django.http import request
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView
# from django.core.paginator import Paginator
# from django.shortcuts import render, redirect
from django.conf import settings
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, FeedBack,CommentsSportsman, CommentsTrener,CommentsStand
from app.olimp.forms import StandForm, SportsmanForm, TrenerForm, FeedBackForm, CommentsSportsmanForm, CommentsTrenerForm,CommentsStandForm
from django.urls import reverse_lazy
from app.olimp.filters import StandFilter, SportsmanFilter, TrenerFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class StandList(FilterView):
    """Класс вывода всех записей Стэнд(Новости)"""
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


class StandDetail(FormMixin, DetailView):
    """Класс просмотра детализированной страницы Новости(Стэнд)"""
    model = Stand
    context_object_name = "stands"
    template_name = "stand/stand_detail.html"
    pk_url_kwarg = "pk"
    form_class = CommentsStandForm

    def get_success_url(self):
        return reverse_lazy('stand_detail_view', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.stand_name
        context["comments"] = CommentsStand.objects.filter(news=self.object.pk).filter(moderation_is_visible=False)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        form.instance.news = self.object
        form.instance.user_id = self.request.user.id
        form.instance.moderation_is_visible = False
        form.save()
        return super().form_valid(form)


class StandCreateView(LoginRequiredMixin, CreateView):
    """Класс создание поста Стэнд(новости)"""
    model = Stand
    model_form = StandForm
    context_object_name = "stands"
    template_name = "stand/stand_add.html"
    success_url = reverse_lazy("add_stand")
    fields = ["stand_name", "stand_description", "sportsman_id", "view_olimp_id", "medal_id", "date_event", "stand_img"]
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stands"] = self.queryset
        context["title"] = "Добавить новость"
        return context


class SportsmanList(FilterView):
    """Класс вывода всех записей Спортсмена"""
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


class SportsmanDetail(FormMixin, DetailView):
    """Класс просмотра детализированной страницы Спортсмена"""
    model = Sportsman
    context_object_name = "sportsman"
    template_name = "sportsman/sportsman_detail.html"
    pk_url_kwarg = "pk"
    form_class = CommentsSportsmanForm

    def get_success_url(self):
        return reverse_lazy('sportsman_detail_view', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.sportsman_name
        context["comments"] = CommentsSportsman.objects.filter(news=self.object.pk).filter(moderation_is_visible=False)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        form.instance.news = self.object
        form.instance.user_id = self.request.user.id
        form.instance.moderation_is_visible = False
        form.save()
        return super().form_valid(form)


class SportsmanCreateView(LoginRequiredMixin, CreateView):
    """Класс создание поста Спортсмена"""
    model = Sportsman
    model_form = SportsmanForm
    context_object_name = "sportsmans"
    template_name = "sportsman/sportsman_add.html"
    success_url = reverse_lazy("add_sportsman")
    fields = ["sportsman_name", "country_id", "sportsman_birthday", "sportsman_biogrpahy", "view_sports_id",
              "trener_id", "sportsman_img", ]
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sportsman"] = self.queryset
        context["title"] = "Добавить спортсмена"
        return context


class TrenerList(FilterView):
    """Класс вывода всех записей Тренера"""
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


class TrenermanDetail(FormMixin, DetailView):
    """Класс просмотра детализированной страницы Тренера"""
    model = Trener
    context_object_name = "trener"
    template_name = "trener/trener_detail.html"
    pk_url_kwarg = "pk"
    form_class = CommentsTrenerForm

    def get_success_url(self):
        return reverse_lazy('trener_detail_view', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.trener_name
        context["comments"] = CommentsTrener.objects.filter(news=self.object.pk).filter(moderation_is_visible=False)
        context["sports"] = Sportsman.objects.filter(trener_id=self.object.pk).filter(sportsman_is_visible=False)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        form.instance.news = self.object
        form.instance.user_id = self.request.user.id
        form.instance.moderation_is_visible = False
        form.save()
        return super().form_valid(form)


class TrenerCreateView(LoginRequiredMixin, CreateView):
    """Класс создание поста Тренера"""
    model = Trener
    model_form = TrenerForm
    context_object_name = "treners"
    template_name = "trener/trener_add.html"
    success_url = reverse_lazy("add_trener")
    fields = ["trener_name", "club_id", "trener_img"]
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["treners"] = self.queryset
        context["title"] = "Добавить тренера"
        return context


class FeedBackCreateView(CreateView):
    """Класс создание поста Обраятная связь"""
    model = FeedBack
    model_form = FeedBackForm
    context_object_name = "feedback"
    template_name = "feedback/feedback_msg.html"
    success_url = reverse_lazy("feedback")
    fields = ["fb_name", "fb_email", "fb_message", "fb_img", ]
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feedback"] = self.queryset
        context["title"] = "Обратная связь"
        return context
