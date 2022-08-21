from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from app.olimp.models import Stand, Sportsman, ViewOlimp, ViewSports, Trener, Club, Medal


# from django.urls import reverse_lazy
# from app.books.forms import BookForm
# from app.books.filters import BookFilter
# from app.books.validators import validation_book_name

class StandList(FilterView):
    model = Stand
    # filterset_class = StandFilter
    context_object_name = "stands"
    template_name = "stands/stand_list.html"

class StandDetail(DetailView):
    pass

class StandCreateView(CreateView):
    pass
